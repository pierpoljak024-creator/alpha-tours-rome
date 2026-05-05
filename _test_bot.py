"""Test the Modal-deployed Telegram bot"""
import urllib.request
import json
import time

print("=== Step 1: Wake up Modal container ===")
for i in range(5):
    try:
        r = urllib.request.urlopen('https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/health', timeout=30)
        print(f'  [{i+1}] Health: {r.read().decode()}')
    except Exception as e:
        print(f'  [{i+1}] ERROR: {e}')
    time.sleep(1)

print()
print("=== Step 2: Check Telegram for recent bot activity ===")
time.sleep(2)

# Check Telegram API for bot activity
req = urllib.request.Request(
    f'https://api.telegram.org/bot8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk/getUpdates',
    data=b'{"offset": -10}',
    headers={'Content-Type': 'application/json'}
)
r2 = urllib.request.urlopen(req, timeout=30)
data = json.loads(r2.read())

if data.get('ok') and data.get('result'):
    print(f'  Pending updates: {len(data["result"])}')
    for msg in data['result']:
        msg_text = msg.get('message', {}).get('text', '?')
        user = msg.get('message', {}).get('from', {}).get('first_name', '?')
        print(f'  Update {msg["update_id"]}: from={user} msg="{msg_text}"')
else:
    print('  No pending updates')

# Check if bot has any webhook or recent polling
r3 = urllib.request.urlopen(
    f'https://api.telegram.org/bot8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk/getWebhookInfo',
    timeout=30
)
webhook = json.loads(r3.read())
print(f'  Webhook: {json.dumps(webhook["result"], indent=2)}')

print()
print("=== Step 3: Checking if we can get fresh Modal logs ===")
try:
    import subprocess
    result = subprocess.run(
        ['modal', 'app', 'logs', 'alpha-tours-rome-bot'],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
        cwd=r'C:\Users\pierf\AlphaTours-Project'
    )
    # Print last 40 lines of stdout (skip old content)
    lines = result.stdout.split('\n')
    print(f'  Total log lines: {len(lines)}')
    print('  Last 30 lines:')
    for line in lines[-30:]:
        if line.strip():
            print(f'    {line.strip()[:200]}')
except Exception as e:
    print(f'  Error getting logs: {e}')

print()
print("=== DONE ===")
