"""Send a message to the bot and check for response"""
import urllib.request
import json
import time

BOT_TOKEN = "8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk"
CHAT_ID = "5285215270"

print("1. Check Modal health...")
r = urllib.request.urlopen("https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/health", timeout=30)
print(f"   {r.read().decode()}")

print("\n2. Sending test message to bot via Telegram API...")
data = json.dumps({"chat_id": CHAT_ID, "text": "Hi from test!"}).encode()
req = urllib.request.Request(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data=data,
    headers={"Content-Type": "application/json"}
)
r2 = urllib.request.urlopen(req, timeout=30)
resp = json.loads(r2.read())
print(f"   Sent: {resp.get('ok')}")

print("\n3. Wait 10s for bot to process...")
time.sleep(10)

print("4. Check for new updates...")
offset = -1
req3 = urllib.request.Request(
    f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}",
    headers={"Content-Type": "application/json"}
)
r3 = urllib.request.urlopen(req3, timeout=30)
updates = json.loads(r3.read())
for u in updates.get("result", []):
    msg = u.get("message", {})
    text = msg.get("text", "")
    date = msg.get("date", 0)
    print(f"   Update {u['update_id']}: '{text}' at {date}")
    # Check if there's a reply
    reply = msg.get("reply_to_message")
    if reply:
        print(f"     (reply to: {reply.get('text', '?')})")

print(f"\n5. Total updates: {len(updates.get('result', []))}")

# Check if there are any replies FROM the bot (not from you)
print("\n6. Check for bot replies (getUpdates with higher offset)...")
# Try getting all recent updates
req4 = urllib.request.Request(
    f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates",
    headers={"Content-Type": "application/json"}
)
r4 = urllib.request.urlopen(req4, timeout=30)
all_updates = json.loads(r4.read())
for u in all_updates.get("result", []):
    msg = u.get("message", {})
    text = msg.get("text", "")
    fwd = msg.get("forward_from", {})
    print(f"   ID:{u['update_id']} msg:'{text}' from:{msg.get('from',{}).get('id','?')}")

print("\n=== Done ===")
