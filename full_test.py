"""Full test: send message to bot and wait for reply"""
import urllib.request
import json
import time

BOT_TOKEN = "8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk"
CHAT_ID = "5285215270"

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    if offset:
        url += f"?offset={offset}"
    req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
    r = urllib.request.urlopen(req, timeout=30)
    return json.loads(r.read())

def send_message(text, chat_id=CHAT_ID):
    data = json.dumps({"chat_id": chat_id, "text": text}).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    r = urllib.request.urlopen(req, timeout=30)
    return json.loads(r.read())

print("=== Step 1: Get initial update offset ===")
updates = get_updates()
last_offset = max((u["update_id"] for u in updates.get("result", [])), default=0)
print(f"  Last update ID: {last_offset}")

print("\n=== Step 2: Send message to bot ===")
send_message("Ciao! Can you recommend a tour for me?")
print("  Message sent!")

print("\n=== Step 3: Wait 30s for bot to reply ===")
for i in range(10):
    time.sleep(3)
    updates = get_updates(offset=last_offset + 1)
    new_updates = updates.get("result", [])
    
    if new_updates:
        for u in new_updates:
            msg = u.get("message", {})
            text = msg.get("text", "")
            user_id = msg.get("from", {}).get("id", 0)
            username = msg.get("from", {}).get("first_name", "?")
            print(f"  [{i+1}/10] Update {u['update_id']}: '{text}' from {username} (ID:{user_id})")
            last_offset = max(last_offset, u["update_id"])
        break
    else:
        print(f"  [{i+1}/10] No new updates yet...")

print("\n=== Step 4: Final check ===")
r = urllib.request.urlopen("https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/health", timeout=30)
print(f"  Health: {r.read().decode()}")

print("\n=== DONE ===")
