# 🤖 Alpha Tours Rome — AI Concierge Bot

Your 24/7 automated Telegram assistant that knows everything about Alpha Tours Rome and helps customers find the perfect tour.

---

## 🚀 How to Start

### ✅ Quick Start (Laptop On)
1. **Double-click** the **"Start Alpha Tours Bot"** icon on your Desktop
2. A black terminal window will open — this is your bot coming to life
3. Wait ~10 seconds, then message your bot on Telegram
4. **To stop**: Close the terminal window (or press Ctrl+C)

### ☁️ Cloud Mode (24/7 — No Laptop Needed)
See the **Modal Cloud Deployment** section below.

---

## 📁 Important Files

| File | What it does |
|------|-------------|
| `start_telegram_gateway.py` | Launches the bot (double-click this) |
| `SOUL.md` (in `C:\Users\pierf\.hermes\`) | **The bot's personality & knowledge** ⭐ |
| `.env` | Your secret API keys (Telegram + OpenRouter) |
| `AGENTS.md` | Backup copy of the bot's tour knowledge |
| `README.md` | This file! |

---

## ✏️ How to Update Tours or Change the Bot's Voice

The bot's entire personality and knowledge come from **one file**:

📄 **`C:\Users\pierf\.hermes\SOUL.md`**

### To add a new tour:
1. Open `SOUL.md` with Notepad
2. Find the right category (e.g. `### GOLF CART TOURS`)
3. Add your new tour using the same format:
   ```
   8. **New Tour Name** — 2 hours, Private
      → https://alphatoursrome.com/tours/new-tour.html
   ```
4. Save the file and restart the bot

### To change how it talks:
Just edit the **BRAND VOICE** section at the top of `SOUL.md`.
Want it more formal? More playful? Different emojis? Edit and save!

### After any change:
- **If running locally**: Close the terminal window, then double-click the Desktop icon again
- **If running on Modal**: Re-deploy (see Modal section)

---

## 💬 What Customers See

When someone messages your Telegram bot:

1. They ask a question (e.g. *"What tours do you offer?"*)
2. The AI brain processes it using your SOUL.md knowledge
3. It replies instantly with tour info, booking links, and the Alpha Tours brand voice
4. If it can't help, it directs them to WhatsApp: **+39 375 829 7864**

---

## ☁️ Modal Cloud Deployment (24/7 — Live! 🚀)

**Your bot is LIVE:** https://modal.com/apps/pierpoljak024/main/deployed/alpha-tours-rome-bot

### What is Modal?
Modal is a cloud service that runs your bot on their servers forever — your laptop can be off, asleep, or anywhere. The bot keeps working 24/7.

### Cost
- **Free tier**: $30/month credit
- **This bot costs**: ~$0.50/month → **essentially free forever** ☁️

### How to Update the Cloud Bot

1. Edit `C:\Users\pierf\.hermes\SOUL.md` or `C:\Users\pierf\.hermes\config.yaml`
2. Open a terminal and run:
   ```
   cd C:\Users\pierf\AlphaTours-Project
   modal deploy modal_deploy.py
   ```
3. Wait ~30 seconds — the bot restarts with the new personality ✨

*Only updates if SOUL.md or config.yaml changed — cached image is reused.*

### Monitor the Bot
- **Dashboard:** https://modal.com/apps/pierpoljak024/main/deployed/alpha-tours-rome-bot
- **Logs:** `modal logs alpha-tours-rome-bot run_bot`

---

## 🔧 Troubleshooting

**Bot not responding on Telegram?**
1. Check if the terminal window is still open (if running locally)
2. Make sure your laptop is connected to the internet
3. Restart the bot by double-clicking the Desktop icon

**Bot gives wrong answers?**
- Edit `SOUL.md` to fix what it's getting wrong
- Restart the bot after saving

**Something broken?**
- Open WhatsApp and message Pier +39 375 829 7864

---

## 📝 Notes

- **API Keys** are stored in `.env` — keep this file safe (don't share it online)
- **Conversation history** is saved in `C:\Users\pierf\.hermes\sessions\`
- The bot runs on **Google Gemini 2.0 Flash** via OpenRouter (fast and cheap)
- You can change the AI model in `C:\Users\pierf\.hermes\config.yaml`

---

*Built with ❤️ for Alpha Tours Rome — Local Guides · Authentic Tours · Memorable Moments*
