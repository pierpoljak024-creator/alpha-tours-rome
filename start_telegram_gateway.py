"""Start Hermes Telegram gateway for Alpha Tours Rome."""
import sys, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Load secrets from .env file
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            key, _, value = line.partition('=')
            os.environ.setdefault(key.strip(), value.strip())

os.chdir(r'c:\Users\pierf\AlphaTours-Project')
os.environ.setdefault('GATEWAY_ALLOW_ALL_USERS', 'true')

from hermes_cli.main import main
import sys as s
s.argv = ['hermes', 'gateway', 'run', '--accept-hooks']
main()
