import urllib.request
try:
    r = urllib.request.urlopen("https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/health", timeout=15)
    print(r.read().decode())
except Exception as e:
    print(f"FAIL: {e}")
