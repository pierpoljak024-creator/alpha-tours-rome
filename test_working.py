"""Send test message and check Modal logs for response"""
import urllib.request
import json
import time

BOT_TOKEN = "8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk"
CHAT_ID = "5285215270"

# 1. Read pre-test Modal logs
print("=== PRE-TEST LOGS ===")
r = urllib.request.urlopen("https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/logs", timeout=30)
pre_logs = r.read().decode()
print(f"Pre-test log lines: {len([l for l in pre_logs.split(chr(10)) if l.strip()])}")
print("Last 3 lines:")
for l in pre_logs.split(chr(10))[-3:]:
    if l.strip():
        print(f"  {l}")

# 2. Send message 
print("\n=== SENDING MESSAGE ===")
payload = json.dumps({"chat_id": CHAT_ID, "text": "Ciao! Can you recommend a good tour for my first time in Rome?"})
req = urllib.request.Request(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data=payload.encode(),
    headers={"Content-Type": "application/json"}
)
r = urllib.request.urlopen(req, timeout=30)
resp = json.loads(r.read())
print(f"Sent: {resp.get('ok')}, msg_id: {resp.get('result',{}).get('message_id','?')}")

# 3. Wait and check Modal logs again
print("\n=== WAITING 20s ===")
time.sleep(20)

print("\n=== POST-TEST LOGS ===")
r = urllib.request.urlopen("https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/logs", timeout=30)
post_logs = r.read().decode()

# Show what's new since pre-test
if post_logs != pre_logs:
    print("=== NEW LOG CONTENT ===")
    new_lines = post_logs[len(pre_logs):]
    for l in new_lines.split(chr(10)):
        if l.strip():
            print(f"  {l}")
else:
    print("NO NEW LOGS - bot may not have received the message")
    print(f"File sizes: pre={len(pre_logs)}, post={len(post_logs)}")

# 4. Check Telegram for bot reply 
print("\n=== CHECKING TELEGRAM UPDATES ===")
req2 = urllib.request.Request(
    f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates",
    headers={"Content-Type": "application/json"}
)
r2 = urllib.request.urlopen(req2, timeout=30)
updates = json.loads(r2.read())
for u in updates.get("result", []):
    msg = u.get("message", {})
    text = msg.get("text", "")
    fname = msg.get("from", {}).get("first_name", "?")
    is_bot = msg.get("from", {}).get("is_bot", False)
    msg_id = msg.get("message_id", "?")
    reply_to = msg.get("reply_to_message")
    print(f"  msg_id={msg_id} bot={is_bot} from={fname}")
    print(f"    text: {text}")
    if reply_to:
        print(f"    reply_to: {reply_to.get('text', '?')}")

print("\n=== DONE ===")
