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

group_metas = [-1001707678506]  

group_ids = [-1001510261210, -1001634555044, -1002422141340, -1001527830462] 

TARGET_GROUPS = [-1002288646386, -1001202193997]

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
            await asyncio.sleep(random.randint(600,1200))

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
