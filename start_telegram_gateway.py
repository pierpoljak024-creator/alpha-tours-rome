"""Start Hermes Telegram gateway for Alpha Tours Rome."""
import sys, os

sys.stdout.reconfigure(encoding='utf-8')

os.chdir(r'c:\Users\pierf\AlphaTours-Project')
os.environ['OPENROUTER_API_KEY'] = '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'
os.environ['TELEGRAM_BOT_TOKEN'] = '8707235452:AAEvAD6-ppKbCLzgigPWrKvg_BINZzCdOkk'
os.environ['GATEWAY_ALLOW_ALL_USERS'] = 'true'

from hermes_cli.main import main
import sys as s
s.argv = ['hermes', 'gateway', 'run', '--accept-hooks']
main()
