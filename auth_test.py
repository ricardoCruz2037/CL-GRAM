from dotenv import load_dotenv
from telethon import TelegramClient
import os, asyncio

# Cargar las variables del .env
load_dotenv("config/.env")

# Convierte 'API_ID' a entero
api_id = int(os.getenv("API_ID"))

# Lee las variables
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")

#Crear el cliente Telethon
client = TelegramClient(session_name, api_id, api_hash)

# Conectar e imprimir la info
async def main():
    await client.start()
    me = await client.get_me()
    print(me.stringify())
asyncio.run(main())
