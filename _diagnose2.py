"""Diagnose Hermes - check state_meta and .hermes config"""
import sqlite3, json, os

# Check state_meta table
conn = sqlite3.connect(r'C:\Users\pierf\.hermes\state.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM state_meta")
rows = cursor.fetchall()
print("=== state_meta ===")
for row in rows:
    for i, val in enumerate(row):
        if val:
            print(f"  [{i}]: {str(val)[:500]}")

conn.close()

# Check if gateway_state.json has more detail
print("\n=== gateway_state.json full ===")
with open(r'C:\Users\pierf\.hermes\gateway_state.json') as f:
    print(json.dumps(json.load(f), indent=2))

# Check the .env file in .hermes
print("\n=== .hermes/.env ===")
with open(r'C:\Users\pierf\.hermes\.env') as f:
    print(f.read())

# Check how TELEGRAM_BOT_TOKEN is referenced in state
print("\n=== Checking all files for TELEGRAM_BOT_TOKEN references ===")
for root, dirs, files in os.walk(r'C:\Users\pierf\.hermes'):
    for fname in files:
        if fname.endswith('.json'):
            fpath = os.path.join(root, fname)
            with open(fpath) as f:
                content = f.read()
                if 'TELEGRAM_BOT_TOKEN' in content or 'bot_token' in content.lower() or '8707235' in content:
                    print(f"  {fpath}: contains token reference")

# Check if there's a gateways config directory
print("\n=== .hermes/gateways directory ===")
gw_dir = r'C:\Users\pierf\.hermes\gateways'
if os.path.isdir(gw_dir):
    for f in os.listdir(gw_dir):
        print(f"  {f}")
        with open(os.path.join(gw_dir, f)) as fh:
            print(f"    {fh.read()[:500]}")
else:
    print("  (no gateways directory)")
