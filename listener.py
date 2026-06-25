from telethon import TelegramClient, events
from dotenv import load_dotenv
from telethon.tl.types import  User, Channel
import os, asyncio
import subprocess

load_dotenv("config/.env")

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)

async def handler(event):
    sender = await event.get_sender()  # Obtiene el remitente del mensaje

    if isinstance(sender, Channel):
        contact_name = sender.title
    elif sender.username is None:  # Reemplaza con el nombre de usuario del remitente
        contact_name = f"{sender.first_name} {sender.last_name or ''}".strip()
    else:
        contact_name = sender.username

    subprocess.Popen([
    "kitty",
    "--single-instance",
    "--instance-group", "clgram",
    "python", "chat.py",
    contact_name
    ]) 

async def main():
    await client.start()
    await client.run_until_disconnected()
    
asyncio.run(main())
