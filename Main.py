import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Environment variables se config lena
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")

# Telegram client banayein
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# Message handler
@client.on(events.NewMessage)
async def handler(event):
    await event.reply("Hello from Railway bot!")

# Bot start karna
client.start()
client.run_until_disconnected()
