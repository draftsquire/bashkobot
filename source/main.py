from telethon.sync import TelegramClient, events
from dotenv import load_dotenv
import os
import asyncio

os.environ.clear()
load_dotenv(override=True)

TG_API_ID = os.environ.get("TG_API_ID")
TG_API_HASH = os.environ.get("TG_API_HASH")
print(TG_API_ID)
print(TG_API_HASH)

async def main():
    client = TelegramClient('baskobot', TG_API_ID, TG_API_HASH)
    await client.start()
    await client.send_message('me', 'Hello, myself!')
    # await print(client.download_profile_photo('me'))
    return

asyncio.run(main())
# @client.on(events.NewMessage(pattern='(?i).*Hello'))
# async def handler(event):
#     await event.reply('Hey!')

# client.run_until_disconnected()
