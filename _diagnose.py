"""Diagnose Hermes state - check what's in the database"""
import sqlite3, json

# Check state.db for platform/telegram config
conn = sqlite3.connect(r'C:\Users\pierf\.hermes\state.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cursor.fetchall()]
print("Tables:", tables)

for table in tables:
    cursor.execute(f'SELECT * FROM "{table}"')
    rows = cursor.fetchall()
    if rows:
        cursor.execute(f'PRAGMA table_info("{table}")')
        cols = [c[1] for c in cursor.fetchall()]
        print(f'\n=== {table} ===')
        for row in rows:
            for i, val in enumerate(row):
                s = str(val)
                if any(kw in s.lower() for kw in ['telegram', 'gateway', 'platform', '5285215270', 'bot_token']):
                    print(f'  {cols[i]}: {s[:300]}')

conn.close()

# Also check what's in kanban.db
print("\n\n=== kanban.db ===")
conn2 = sqlite3.connect(r'C:\Users\pierf\.hermes\kanban.db')
cursor2 = conn2.cursor()
cursor2.execute("SELECT name FROM sqlite_master WHERE type='table'")
for t in [r[0] for r in cursor2.fetchall()]:
    cursor2.execute(f'PRAGMA table_info("{t}")')
    cols = [c[1] for c in cursor2.fetchall()]
    cursor2.execute(f'SELECT * FROM "{t}"')
    rows = cursor2.fetchall()
    print(f'\n=== {t} (cols: {cols}) ===')
    for row in rows[:3]:
        for i, val in enumerate(row):
            s = str(val)
            if any(kw in s.lower() for kw in ['telegram', 'gateway', 'platform', 'bot_token', 'config']):
                print(f'  {cols[i]}: {s[:300]}')
conn2.close()
