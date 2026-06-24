# Changelog

All notable changes to CL-GRAM will be documented in this file.

---

## [v0.1] — Project Setup & Authentication — 2026-06-24

### Summary

Initial project setup: environment isolation, dependency installation, Telegram API credentials, and a working authentication test script.

---

### README and .gitignore

**README**

`.md` file to present the project — covers description, features, tech stack, prerequisites, project structure, installation, usage, configuration, and roadmap.

**gitignore**

`.gitignore` configured to never track two critical categories:

- Credential files (`.env`) — contains the environment variables `API_ID`, `API_HASH` and `SESSION_NAME` with the Telegram User API (MTProto) credentials as values.
- Session files (`.session`) — contains an active authenticated Telegram session. If leaked, it grants full access to the account without requiring a password or 2FA.

---

### Environment Isolation

Isolated Python installation to avoid conflicts with the native OS interpreter, using `pyenv` and `venv`.

**pyenv** — Python multiversion manager. Used to install Python 3.13 scoped to the project directory (`CL-GRAM/`), leaving the system interpreter untouched.

**venv** — Native Python module for creating virtual environments with their own `pip` and `site-packages`, isolating project dependencies from the global environment.

---

### Telethon and python-dotenv

**Telethon** — Python implementation of Telegram's proprietary binary protocol MTProto. Allows operating as a real Telegram client with access to private chats, message history, contacts, and real-time events.

**python-dotenv** — Utility that reads `.env` files and loads their key-value pairs as process environment variables.

**requirements.txt** — Project dependency manifest. Generated with `pip freeze`, it captures the exact versions installed in the active virtual environment, making the setup fully reproducible on any machine via `pip install -r requirements.txt`.

---

### Telegram User API — MTProto

The full API used by official Telegram clients — not to be confused with the Bot API, which is a simplified REST interface with limited access.

Access requires registering an application at [my.telegram.org](https://my.telegram.org), which generates two credentials:

- `API_ID` — numeric identifier of the registered application
- `API_HASH` — application secret, equivalent to a password

These credentials identify the *application*, not the user account. Account authentication happens separately at runtime.

---

### Environment Variables — .env

The `.env` + `.env.example` pattern is an industry standard convention documented in the **12-factor app** methodology:

- Source code goes to the repository; sensitive configuration does not.
- `.env.example` acts as documentation — it shows which variables exist without exposing real values.
- Variables follow the **SCREAMING_SNAKE_CASE** convention.

One important technical detail: `os.getenv()` always returns strings. Telethon requires `API_ID` as an integer, so an explicit cast with `int()` is necessary — without it, the connection fails silently.

---

### Authentication Script — auth_test.py

Temporary script written to verify that the full stack (credentials → Telethon → Telegram API) works correctly before building the actual application.

**`client.start()`** — Performs the MTProto handshake with Telegram's servers. Handles phone number input, OTP code delivery, and 2FA password if enabled. It is a high-level abstraction method for the full authentication flow.

After a successful connection, Telethon persists the session in a `.session` file — a lightweight SQLite database storing the session keys. On subsequent runs, these keys are reused so authentication is not required again.

**`get_me()`** — API call that returns the authenticated account's `User` object, confirming the session is active and valid.

**`stringify()`** — Serializes the `User` object into a human-readable string for debugging.

---

### Files Added

| File | Description |
|------|-------------|
| `README.md` | Project presentation and documentation |
| `.gitignore` | Excludes credentials and session files from version control |
| `.python-version` | pyenv local version pin (Python 3.13) |
| `venv/` | Virtual environment directory (not tracked) |
| `requirements.txt` | Pinned project dependencies |
| `config/.env` | Environment variables — credentials (not tracked) |
| `config/.env.example` | Environment variable template (tracked) |
| `auth_test.py` | Temporary authentication verification script |
