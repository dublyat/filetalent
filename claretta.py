from telethon import TelegramClient, events
import asyncio
import random
import getpass
from random import randint
from time import sleep
from telethon import types
from telethon.errors import SessionPasswordNeededError

###############INPUT PART###############

api_id = '28119255'
api_hash = '337f330b7ab0c169c6296bc80338c6fd'
phone = '+6283185102534'

group_ids = [-1001707678506, -1001510261210, -1001634555044, -1002422141340]  

automsg = ["wanna call? @babyeta", "@babyeta 🤪",
"aht aht mass @babyeta", "@babyeta 😉",
"sini ak temenin @babyeta", "@babyeta 😋",
"kolsegs @babyeta", "@babyeta 🤤",
"ak tmnin crttt @babyeta", "@babyeta 💋",
"crtin foto ak dong @babyeta", "@babyeta 🥺",
"call yuu @babyeta", "@babyeta 🥰",
"kolsegs kaa @babyeta", "@babyeta 😘",
"vcsange yuu @babyeta", "@babyeta 😗",
"sini ak tmnin vc @babyeta", "@babyeta 😻"
]

client = TelegramClient('claretta', api_id, api_hash)

###############INPUT PART###############

async def send_random_messages():
      while True:
        for group_id in group_ids:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_id, message_auto)        
            await asyncio.sleep(random.randint(90,150))


async def main():
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input('Enter the code: ')
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = getpass.getpass('ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀssᴡᴏʀᴅ: ')
            await client.sign_in(password=password)

    print("sᴛᴀʀᴛɪɴɢ ᴄʟᴀʀᴇᴛᴛᴀ")


    asyncio.create_task(send_random_messages())
    await client.run_until_disconnected()

asyncio.run(main())
