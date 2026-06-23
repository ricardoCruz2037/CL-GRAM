# 📡 CL-GRAM

> Telegram messaging integration within CLI (Kitty terminal) for specific contacts.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Telegram](https://img.shields.io/badge/Telegram-User%20API-26A5E4?logo=telegram)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

---

## 📌 Description

Read and respond to Telegram messages for specific contacts directly from the Linux CLI.

Once a message arrives from a whitelisted contact, a new Kitty window opens and prompts you to reply or dismiss. If you choose to reply, the window becomes an interactive chat session — type your message and hit Enter to send. That's it.

This started as a personal idea during free time — a fun way to make terminal interaction feel a bit more alive. No overengineering intended; just a clean, lightweight tool for anyone who enjoys living in the terminal.

---

## ✨ Features

- [ ] RF-01 — Telegram authentication via User API
- [ ] RF-02 — Real-time message listening
- [ ] RF-03 — Whitelist for specific contacts
- [ ] RF-04 — Automatic Kitty window on incoming message
- [ ] RF-05 — Recent message history display
- [ ] RF-06 — Send messages from CLI
- [ ] RF-07 — Sticker support (prints sticker name only)
- [ ] RF-08 — `/exit` command to close the conversation

---

## 🧰 Tech Stack

| Component | Technology              |
|-----------|-------------------------|
| Language  | Python 3.13             |
| API       | Telegram User API (MTProto) |
| Library   | Telethon                |
| Terminal  | Kitty                   |
| OS        | Ubuntu 24.04            |
| Config    | `.env` + `whitelist.json` |

---

## 📋 Prerequisites

- Python 3.13+
- [Kitty terminal](https://sw.kovidgoyal.net/kitty/)
- A Telegram account
- Telegram API credentials → [my.telegram.org](https://my.telegram.org)

---

## 📁 Project Structure

```
CL-GRAM/
├── listener.py         # Daemon — listens for incoming messages
├── chat.py             # Chat window — one instance per contact
├── config/
│   ├── whitelist.json  # Allowed contacts list
│   └── .env.example    # Environment variable template (no real credentials)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/ricardoCruz2037/CL-GRAM.git
cd CL-GRAM

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp config/.env.example .env
# Edit .env with your API_ID and API_HASH from my.telegram.org
```

---

## 🚀 Usage

```bash
# Start the listener daemon in the background
python listener.py &

# When a message arrives from a whitelisted contact,
# Kitty automatically opens a conversation window.

# Inside the chat window:
# - Type your message and press Enter to send
# - Type /exit or /quit to close the conversation
```

---

## 🔐 Configuration

### Environment variables (`.env`)

```env
API_ID=YOUR_API_ID
API_HASH=YOUR_API_HASH
```

### Contact whitelist (`config/whitelist.json`)

```json
{
  "contacts": [
    "username1",
    "username2"
  ]
}
```

> ⚠️ **Never push your real `.env` to the repository.** It is included in `.gitignore`.  
> ⚠️ **Same applies to `*.session` files** — Telethon stores your authenticated session there.

---

## 🗺️ Roadmap

- [x] Requirements gathering
- [ ] v0.1 — Authentication and basic listener
- [ ] v0.2 — Kitty window launch + reply prompt
- [ ] v0.3 — Conversation loop + message sending
- [ ] v0.4 — Whitelist filter + sticker handling
- [ ] v1.0 — Stable, documented, with proper error handling

---

## 👤 Author

**Ricardo López Cruz**  
TICs Engineering Student — ITSOEH / TECNM  
[GitHub](https://github.com/ricardoCruz2037) · [LinkedIn](https://www.linkedin.com/in/richard-lc2037222004)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).