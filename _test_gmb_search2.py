"""Test Google My Business - googleLocations:search with correct field names."""
import json, urllib.request, urllib.parse, sys, time

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

# 2. Try googleLocations:search with correct field names
# Google API uses snake_case for location fields
print("\n=== googleLocations:search by website ===")
body2 = json.dumps({
    "location": {
        "language_code": "en",
        "website_url": "https://alphatoursrome.com",
        "phone_number": "+393758297864"
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
        print(f"   Full response: {json.dumps(resp2, indent=2)[:2000]}")
    else:
        print(f"   No location returned. Response: {json.dumps(resp2, indent=2)[:1000]}")
except urllib.error.HTTPError as e:
    body2resp = e.read().decode()
    print(f"❌ HTTP {e.code}: {body2resp[:1000]}")
    print(f"\n   Wait 120s then retry...")
    time.sleep(120)
    print("   Retrying...")
    try:
        req2 = urllib.request.Request(url2, data=body2, headers=headers)
        resp2 = json.loads(urllib.request.urlopen(req2).read())
        print(f"   Response: {json.dumps(resp2, indent=2)[:1000]}")
    except urllib.error.HTTPError as e2:
        print(f"   Still HTTP {e2.code}")
        print(e2.read().decode()[:300])

# 3. Also try without website, just phone
print("\n=== googleLocations:search by phone only ===")
body3 = json.dumps({
    "location": {
        "language_code": "en",
        "phone_number": "+393758297864"
    }
}).encode()
try:
    req3 = urllib.request.Request(url2, data=body3, headers=headers)
    resp3 = json.loads(urllib.request.urlopen(req3).read())
    print(f"   Response: {json.dumps(resp3, indent=2)[:1000]}")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP {e.code}: {e.read().decode()[:300]}")
