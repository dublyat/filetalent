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

group_metas = [-1001707678506]  

group_ids = [-1001510261210, -1001634555044, -1002422141340, -1001527830462] 

TARGET_GROUPS = [-1002288646386, -1001202193997]


automsg = ["wanna kolsegs byy? @babyeta",
"aht aht masukin mass @babyeta",
"sini ak temenin enaaa @babyeta",
"ak tmnin crttt byy @babyeta",
"vcsange byyy @babyeta",
"-1 co hyprrr 🥵 chat sayangg @babyeta",
"-1 co angeee sinii 🤪 @babyeta",
"-1 co yang mau ak goyangin 😋 @babyeta",
"-1 co hypeersxx sinii 😛 @babyeta",
"-1 co vcsangeee 🥵 @babyeta",
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

is_forwarding_active = False

############### BOT SPAM ###############

async def send_random_messages():
      while True:
        for group_id in group_ids:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_id, message_auto)        
            await asyncio.sleep(random.randint(300,900))

async def send_random_messages2():
      while True:
        for group_meta in group_metas:
            message_auto = random.choice(automsg)
            message = await client.send_message(group_meta, message_auto)        
            await asyncio.sleep(random.randint(600,900))

############### BOT FORWARD ###############

async def forward_loop():
    global is_forwarding_active
    group_index = 0

    while is_forwarding_active:
        saved = await client.get_messages('me', limit=20)
        if saved:
            msg = random.choice(saved)
            target = TARGET_GROUPS[group_index]

            await client.forward_messages(
                entity=target,
                messages=msg 
            )
            print(f"Forwarded message ID {msg.id} to {target}")

            group_index = 1 - group_index
            await asyncio.sleep(random.randint(600,1200))


@client.on(events.NewMessage(pattern='/blackcat'))
async def cmd_start(event):
    global is_forwarding_active
    if not is_forwarding_active:
        is_forwarding_active = True
        await event.respond("ᴇɴɢɪɴᴇ sᴛᴀʀᴛᴇᴅ")
        asyncio.get_event_loop().create_task(forward_loop())
    else:
        await event.respond("ᴇɴɢɪɴᴇ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ")

############### LOGIN PART ###############

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

    print("sᴛᴀʀᴛɪɴɢ ʀᴇʀᴇ")

    asyncio.create_task(send_random_messages())

    asyncio.create_task(send_random_messages2())
      
    await client.run_until_disconnected()

asyncio.run(main())
