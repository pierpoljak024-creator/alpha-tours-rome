"""Test Google My Business API with OAuth refresh token."""
import json, os, urllib.request
from urllib.parse import urlencode
from pathlib import Path

TOKEN_FILE = Path("C:/Users/pierf/AlphaTours-Project/google-business-oauth-token.json")
token_data = json.loads(TOKEN_FILE.read_text())

CID = token_data["client_id"]
CSEC = token_data["client_secret"]
REFRESH = token_data["refresh_token"]

# 1. Get access token
body = urlencode({
    "client_id": CID, "client_secret": CSEC,
    "refresh_token": REFRESH, "grant_type": "refresh_token",
}).encode()
req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body,
    headers={"Content-Type": "application/x-www-form-urlencoded"})
resp = json.loads(urllib.request.urlopen(req).read())
access_token = resp.get("access_token")
print(f"Access token: {access_token[:30]}...")

headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

# 2. List accounts
print("\n=== My Business API v1: Accounts ===")
req = urllib.request.Request("https://mybusinessaccountmanagement.googleapis.com/v1/accounts", headers=headers)
resp = json.loads(urllib.request.urlopen(req).read())
print(json.dumps(resp, indent=2)[:2000])
