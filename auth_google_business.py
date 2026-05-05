"""One-time OAuth2 setup for Google Business Profile API.
Run this locally ONCE to generate a refresh token.
"""
import os
import json
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/business.manage"]

CLIENT_CONFIG = {
    "installed": {
        "client_id": "723098435736-hb10eius0c5rform1j56b1bu81tjb13f.apps.googleusercontent.com",
        "project_id": "alpha-tours-paperclip",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": ["http://localhost"]
    }
}

TOKEN_FILE = Path(os.path.dirname(os.path.abspath(__file__))) / "google-business-oauth-token.json"

def main():
    creds = None
    from google.oauth2.credentials import Credentials

    if TOKEN_FILE.exists():
        with open(TOKEN_FILE) as f:
            creds_data = json.load(f)
        creds = Credentials.from_authorized_user_info(creds_data, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(CLIENT_CONFIG, SCOPES)
            creds = flow.run_local_server(port=0, open_browser=True)

        token_data = {
            "token": creds.token,
            "refresh_token": creds.refresh_token,
            "token_uri": creds.token_uri,
            "client_id": creds.client_id,
            "client_secret": creds.client_secret,
            "scopes": creds.scopes,
            "expiry": creds.expiry.isoformat() if creds.expiry else None
        }
        with open(TOKEN_FILE, "w") as f:
            json.dump(token_data, f, indent=2)

        print(f"\nToken saved to: {TOKEN_FILE}")
        print(f"refresh_token: {creds.refresh_token[:20]}...")
        print("\nCopy this refresh_token into modal_deploy.py:")
        print(f"  '{creds.refresh_token}'")
    else:
        print(f"Valid token already exists at: {TOKEN_FILE}")
        print(f"refresh_token: {creds.refresh_token[:20]}...")

if __name__ == "__main__":
    main()
