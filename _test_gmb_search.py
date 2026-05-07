"""Test Google My Business - try googleLocations:search to find the business by website/phone."""
import json, urllib.request, urllib.parse, os, sys, time

# Creds
CLIENT_ID = "723098435736-hb10eius0c5rform1j56b1bu81tjb13f.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//096WoECPUC0v5CgYIARAAGAkSNwF-L9Ir7d7_gstTSuEvDMWSXgGvWkZ8M__UYMMhBDXy5T8VyiO5x7RW2B3_wuYDsTh436QAmC0"

# 1. Get access token
body = urllib.parse.urlencode({
    "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN, "grant_type": "refresh_token",
}).encode()
try:
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    resp = json.loads(urllib.request.urlopen(req).read())
    token = resp.get("access_token")
    print(f"✅ Token obtained: {token[:30]}...")
except Exception as e:
    print(f"❌ OAuth error: {e}")
    sys.exit(1)

headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# 2. Try googleLocations:search instead of accounts listing
print("\n=== googleLocations:search by website ===")
body2 = json.dumps({
    "location": {
        "websiteUrl": "https://alphatoursrome.com",
        "phoneNumbers": ["+393758297864"],
        "locationName": "Alpha Tours Rome",
        "languageCode": "en"
    }
}).encode()
url2 = "https://mybusinessbusinessinformation.googleapis.com/v1/googleLocations:search"
try:
    req2 = urllib.request.Request(url2, data=body2, headers=headers)
    resp2 = json.loads(urllib.request.urlopen(req2).read())
    loc = resp2.get("location")
    if loc:
        print(f"✅ Found! Name: {loc.get('name')}")
        print(f"   Title: {loc.get('title')}")
        print(f"   Phone: {loc.get('phoneNumbers',{}).get('primaryPhone','')}")
        print(f"   Website: {loc.get('websiteUrl','')}")
    else:
        print(f"   Response: {json.dumps(resp2, indent=2)[:1000]}")
except urllib.error.HTTPError as e:
    body2resp = e.read().decode()
    print(f"❌ HTTP {e.code}: {body2resp[:500]}")
    if e.code == 429:
        print("   Still rate limited. Need to wait.")

# 3. Try the v4 accounts API with a longer wait first
print("\n=== Try accounts API with 30s pre-wait ===")
time.sleep(30)
print("   Waited 30s, now trying...")
try:
    req3 = urllib.request.Request("https://mybusinessaccountmanagement.googleapis.com/v1/accounts", headers=headers)
    resp3 = json.loads(urllib.request.urlopen(req3).read())
    print(f"✅ Accounts: {json.dumps(resp3, indent=2)[:500]}")
except urllib.error.HTTPError as e:
    body3 = e.read().decode()
    print(f"❌ HTTP {e.code}: {body3[:300]}")
