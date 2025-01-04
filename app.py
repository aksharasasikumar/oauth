from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import jwt  # To decode the token manually if needed
import os
import random
import string

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a random secret key
app.debug = True

# Set up OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='1044317715591-2gugul58lm0i9csfvellrg20b59dl3v8.apps.googleusercontent.com',
    client_secret='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',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/calendar'
    }
)

@app.route('/')
def index():
    return 'Welcome to OAuth Demo! <a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    # Generate a random nonce and store it in the session
    nonce = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    session['nonce'] = nonce

    # Redirect user to Google for authentication
    redirect_uri = url_for('callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)

@app.route('/callback')
def callback():
    # Exchange the authorization code for an access token
    token = oauth.google.authorize_access_token()

    # Check and print the token for debugging
    print(f"Token received: {token}")
    
    # Decode the token manually to inspect claims
    try:
        decoded_token = jwt.decode(token['id_token'], options={"verify_signature": False})
        print(f"Decoded Token: {decoded_token}")

        # Check the 'iss' claim (issuer) and other claims
        if decoded_token['iss'] !='https://accounts.google.com':
            raise ValueError("Invalid 'iss' claim in token")

        # Validate the nonce (make sure it matches the one stored in the session)
        if decoded_token['nonce'] != session.get('nonce'):
            raise ValueError("Invalid 'nonce' claim in token")

        # Retrieve the user info using the ID token
        user_info = oauth.google.parse_id_token(token, nonce=session.get('nonce'))
        return f"User info: {user_info}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    session.pop('nonce', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()




