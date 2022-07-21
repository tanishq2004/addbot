import logging
from db import *
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
import time

logging.basicConfig(level=logging.INFO)
OWNER_IDS = [2140114063, 2067682959] # edit your id
client = TelegramClient(
    StringSession("Your string session here"),
    api_id=Your api id,
    api_hash="Your api hash"
).start()
# import the time module





#-------------Control Panel----------------#
photo = 'Your Telegraph Link'
TIME_INTERVAL = 1 #An Integer Always add time in minutes
OPTION = 2 #1 for send media + Caption and 2 for only message

#-------------------------------------------#

def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Comrade always OP!!')


t = TIME_INTERVAL*1



  
@client.on(events.NewMessage(pattern="/start"))
async def start(e):
    await e.reply("**Hello, i am an AD promoter bot made by @xD_Comrade**")
    await client(JoinChannelRequest("@Comrade_Selling"))#necessary dont remove

@client.on(events.NewMessage(pattern="/getmsg"))
async def getmsg(e):
    msg = await get_msg()
    await e.reply(f"{msg}")

@client.on(events.NewMessage(pattern="/setmsg"))
async def setmsg(event):
    if event.sender_id not in OWNER_IDS:
        return await event.reply("`Only authorised users can use this command!`")
    reply = await event.get_reply_message()
    if not reply:
        await event.reply("`Reply to the message you want to set!`")
        return
    suc = await insert_msg(reply.text)
    await event.reply(f"`successfully changed message!`")

async def sender():
  
  if OPTION == 1:
    er = 0
    done = 0    
    try:
        msg = await get_msg()
        async for lmao in client.iter_dialogs():
            if lmao.is_group:
                chat = lmao.id
            await client.send_file(
                chat,photo,caption=msg)
            done += 1
    except BaseException as be:
      #  await client.send_message(
          #  "Comrade_Selling",
            #f"Error:\n`{be}`"
        #)
        print(be)
        er += 1
    print(f"done in {done} chats error in {er}")     
        
  elif OPTION == 2 :
    er = 0
    done = 0
    try:
        msg = await get_msg()
        async for lmao in client.iter_dialogs():
            if lmao.is_group:
                chat = lmao.id
            await client.send_message(
                chat,msg)
            done += 1
    except BaseException as be:
        #await client.send_message(
            #"Comrade_Selling",
            #f"Error:\n`{be}`"
       # )
        print(be)
        er += 1
    print(f"done in {done} chats error in {er}")       
  else :
     print('Wrong Option Choosen')
    
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(sender, trigger="interval" ,minutes=TIME_INTERVAL)
scheduler.start()

print('Bot Started, Respect @xD_Comrade')
client.run_until_disconnected()