"""Check Telegram updates to see if bot has replied"""
import urllib.request
import json
import datetime

BOT_TOKEN = "8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
r = urllib.request.urlopen(req, timeout=30)
updates = json.loads(r.read())

print(f"Total updates found: {len(updates.get('result', []))}")
print()

for u in updates.get("result", []):
    msg = u.get("message", {})
    text = msg.get("text", "")
    fname = msg.get("from", {}).get("first_name", "?")
    uid = msg.get("from", {}).get("id", 0)
    is_bot = msg.get("from", {}).get("is_bot", False)
    mid = msg.get("message_id", "?")
    date = msg.get("date", 0)
    
    dt = datetime.datetime.fromtimestamp(date).strftime("%H:%M:%S") if isinstance(date, int) else str(date)
    
    print(f"[id={uid}] {fname} (bot={is_bot}) @ {dt}")
    print(f"  msg_id={mid}: \"{text}\"")
    
    # Check for reply_to
    reply = msg.get("reply_to_message")
    if reply:
        print(f"  reply_to: \"{reply.get('text', '?')}\"")
    print()
