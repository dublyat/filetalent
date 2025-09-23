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

group_metas = [-1001707678506, -1001510261210]  
group_ids = [-1001634555044, -1002422141340]  


automsg = ["wanna kolsegs byy? @babyeta",
"aht aht masukin mass @babyeta",
"sini ak temenin enaaa @babyeta",
"ak tmnin crttt byy @babyeta",
"vcsange byyy @babyeta",
"-1 co hyprrr 🥵 chat sayangg @babyeta",
"-1 co angeee sinii 🤪 @babyeta",
"-1 co yang mau ak goyangin 😋 @babyeta",
"-1 co hypeersxx sinii 😛 @babyeta",
"-1 co vcsangeee 🥵 @babyeta"
"crtin foto ak dong byy @babyeta",
"call sampe crot yuu @babyeta",
"vcsange yuu bareng akuu @babyeta",
"sini ak tmnin vc aht ahtt @babyeta",
"ange bgtt pgn omegg @babyeta",
"wanna kolsegs byy? @babyeta 😋",
"aht aht masukin mass @babyeta 🥺",
"sini ak temenin enaaa @babyeta 🥵",
"ak tmnin crttt byy @babyeta 😖",
"vcsange byyy @babyeta 🤪",
"-1 co hyprrr, chat sayangg @babyeta",
"-1 co angeee sinii @babyeta",
"-1 co yang mau ak goyangin @babyeta",
"-1 co hypeersxx sinii @babyeta",
"-1 co vcsangeee @babyeta",
"crtin foto ak dong byy @babyeta 🤤",
"call sampe crot yuu @babyeta 🍑",
"vcsange yuu bareng akuu @babyeta 🥰",
"sini ak tmnin vc aht ahtt @babyeta 🤪",
"ange bgtt pgn omegg @babyeta 🥺"
]

client = TelegramClient('claretta', api_id, api_hash)

###############INPUT PART###############

async def send_meta_messages():
      while True:
        for group_meta in group_metas:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_meta, message_auto)        
            await asyncio.sleep(random.randint(90,120))

async def send_random_messages():
      while True:
        for group_id in group_ids:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_id, message_auto)        
            await asyncio.sleep(random.randint(90,180))


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

    asyncio.create_task(send_meta_messages())

    asyncio.create_task(send_random_messages())
      
    await client.run_until_disconnected()

asyncio.run(main())
