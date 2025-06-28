import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Get values from Railway environment
API_ID = int(os.getenv("25898893"))
API_HASH = os.getenv("74e7a45148e7e532d432191f69bcfe9c")
SESSION = os.getenv("SESSION")

# Initialize Telegram client
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# Simple message reply handler
@client.on(events.NewMessage)
async def handler(event):
    await event.reply("Hello from SuhailSender Railway Bot!")

# Start the client
client.start()
print("🤖 SuhailSender Bot is now running...")
client.run_until_disconnected()
