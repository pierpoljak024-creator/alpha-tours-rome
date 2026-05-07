#!/usr/bin/env python3
"""Wait 30s then try accounts API."""
import urllib.request, json, urllib.parse, time

CLIENT_ID = "723098435736-hb10eius0c5rform1j56b1bu81tjb13f.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//096WoECPUC0v5CgYIARAAGAkSNwF-L9Ir7d7_gstTSuEvDMWSXgGvWkZ8M__UYMMhBDXy5T8VyiO5x7RW2B3_wuYDsTh436QAmC0"

body = urllib.parse.urlencode({
    "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN, "grant_type": "refresh_token",
}).encode()
req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body,
    headers={"Content-Type": "application/x-www-form-urlencoded"})
resp = json.loads(urllib.request.urlopen(req).read())
token = resp["access_token"]
print("Token OK")
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

print("Trying googleLocations:search with 'title' field...")
url = "https://mybusinessbusinessinformation.googleapis.com/v1/googleLocations:search"

# The error said "location.title" - so try just title
payload = json.dumps({
    "location": {
        "title": "Alpha Tours Rome",
        "languageCode": "en"
    }
}).encode()
try:
    resp = json.loads(urllib.request.urlopen(urllib.request.Request(url, data=payload, headers=headers)).read())
    loc = resp.get("location")
    if loc:
        name = loc.get("name", "")
        print(f"FOUND! Name: {name}")
        print(f"Title: {loc.get('title')}")
        parts = name.split("/")
        if len(parts) >= 4:
            print(f"Account ID: {parts[1]}")
            print(f"Location ID: {parts[3]}")
    else:
        print(f"No match. Response: {json.dumps(resp, indent=2)[:500]}")
except urllib.error.HTTPError as e:
    err = e.read().decode()
    print(f"HTTP {e.code}: {err[:500]}")


