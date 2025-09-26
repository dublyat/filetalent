from telethon import TelegramClient, events
import asyncio
import random
import getpass
from random import randint
from time import sleep
from telethon import types
from telethon.errors import SessionPasswordNeededError

###############INPUT PART###############

api_id = '22033973'
api_hash = '43da19a7b0f4617f4937ff047d820f9d'
phone = '+6283185102531'

group_metas = [-1001707678506, -1001510261210]  

group_ids = [-1001634555044, -1002422141340]  


automsg = ["nenenin dong sayangg @rebeurbae",
"crtin muka aku dongg @rebeurbae",
"sini aku tmnin km crt @rebeurbae",
"vc nakal yuk bebb @rebeurbae",
"vcsange yuu siniii @rebeurbae",
"-1 co hyper yg suka kasarin @rebeurbae 😋",
"-1 co yang tahan 3 ronde @rebeurbae 🥺",
"-1 co hypersx aht ahtt sayang @rebeurbae 🤤",
"-1 co yang mau dienakin @rebeurbae 😜",
"-1 co yang mau vcsex @rebeurbae 🥵",
"udh becek nih beb @rebeurbae",
"pgn di clmekin km @rebeurbae",
"-1 co yang berurat @rebeurbae",
"suka yang berurat @rebeurbae",
"pengen crt di mulut @rebeurbae",
"nenenin dong sayangg 😝 @rebeurbae",
"crtin muka aku dongg 😍 @rebeurbae",
"sini aku tmnin km crt 💋 @rebeurbae",
"vc nakal yuk bebb 🥵 @rebeurbae",
"vcsange yuu siniii 🤭 @rebeurbae",
"-1 co hyper yg suka kasarin @rebeurbae",
"-1 co yang tahan 3 ronde @rebeurbae",
"-1 co hypersx aht ahtt sayang @rebeurbae",
"-1 co yang mau dienakin @rebeurbae",
"-1 co yang mau vcsex @rebeurbae",
"udh becek nih beb 😋 @rebeurbae",
"pgn di clmekin km 😭 @rebeurbae",
"-1 co yang berurat 😫 @rebeurbae",
"suka yang berurat 🥺 @rebeurbae",
"pengen crt di mulut 🤪 @rebeurbae"
]

client = TelegramClient('rere', api_id, api_hash)

###############INPUT PART###############

async def send_random_messages():
      while True:
        for group_id in group_ids:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_id, message_auto)        
            await asyncio.sleep(random.randint(600,1200))

async def send_random_messages2():
      while True:
        for group_meta in group_metas:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_meta, message_auto)        
            await asyncio.sleep(random.randint(360,600))


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

    asyncio.create_task(send_random_messages2())
      
    await client.run_until_disconnected()

asyncio.run(main())
