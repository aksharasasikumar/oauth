Flask OAuth 2.0 Demo

A comprehensive Flask application demonstrating OAuth 2.0 integration with Google for authentication and API access.

 Project Description
This project showcases the implementation of OAuth 2.0 in a Python Flask web application. It allows users to log in using their Google accounts, securely fetches user information (e.g., email, name), and demonstrates how to handle OAuth tokens, session management, and logout functionality.

The application also accesses Google APIs like Calendar and Drive, illustrating how to request and use additional scopes.

 Features
- User authentication via Google OAuth 2.0.
- Secure handling of access tokens using Flask sessions.
- Fetches user profile details (name, email, etc.).
- Demonstrates API access for Google Drive and Calendar.
- Includes logout functionality with session clearing.
- Follows best practices for OAuth implementation, such as nonce validation and secure token exchange.

---

 Prerequisites
Before running this application, ensure you have:
1. Python 3.8 or higher installed.
2. A Google Cloud Console account to create OAuth credentials.
3. Access to a web browser for testing the authentication flow.
Set Up Environment Variables:

Create a .env file in the project directory:
touch .env
Add  Google OAuth credentials to the .env file:
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
Install Dependencies: Install the required Python libraries:
pip install -r requirements.txt
Run the Application: Start the Flask development server:
python app.py
The app will be available at http://127.0.0.1:5000.

Test the OAuth Flow:

Visit the homepage at http://127.0.0.1:5000.
Click on "Login with Google" to start the authentication process.

google Cloud Console Configuration
To use this app, need to configure OAuth credentials in Google Cloud Console:
Go to Google Cloud Console.
Create a new project or select an existing one.
Navigate to APIs & Services > Credentials.
Create an OAuth 2.0 client ID and configure the following:
Authorized redirect URI: Add http://127.0.0.1:5000/callback for local development.
Save the credentials and add the client ID and secret to the .env file.

Project Structure

oauth-flask-app/
├── app.py                  # Flask application code
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (ignored in Git)
├── README.md               # Project documentation
├── .gitignore              # Files and directories to ignore in Git

Technologies Used
Backend: Flask, Authlib
OAuth: Google OAuth 2.0
Language: Python 3.8+
APIs: Google APIs (Profile, Drive, Calendar)

Common Issues and Troubleshooting
Issue: Redirect URI Mismatch
Solution: Ensure the redirect URI in the Google Cloud Console matches http://127.0.0.1:5000/callback.

Issue: "Google hasn’t verified this app" Warning
Solution: Click "Advanced > Proceed (unsafe)" during testing. For production, submit the app for verification in Google Cloud Console.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push the branch (git push origin feature-branch).
Open a pull request.
