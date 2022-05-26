import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from .config import *

 #-------------------------------------------menu Btn-----------------------------------------#

#-------------------------------------------menu Regex-----------------------------------------#         
  
@Client.on_message(filters.regex(pattern="🤴 OWNER 🤴"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=OWNER_BTN
     )
@Client.on_message(filters.regex(pattern="💻 Bot Devs 💻"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(DEV_STICKER),reply_markup=DEV_BTN
     )

@Client.on_message(filters.regex(pattern="👮‍♂️ MemeHub Admins 👮‍♂️"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(ADMIN_STICKER),reply_markup=ADMIN_BTN
     )
    
@Client.on_message(filters.regex(pattern="NEXT 🔜"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='NEXT 🔜',reply_markup=NEXT_1
     )
        
@Client.on_message(filters.regex(pattern="BACK 🔙"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='BACK 🔙',reply_markup=REPLY_BTN
     )

 
 #----------------------------------------------main Cmds---------------------------------------------#

       
        
@Client.on_message(filters.command("start"))
async def start(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    file_id = "CAADBQADVwYAAhCWAVRcksqpPVEWHAI"
    await bot.send_sticker(message.chat.id, file_id, reply_markup=REPLY_BUTTONS)
    text = f"Hi {message.from_user.mention}, Welcome to  MemeHub Telegram 🇱🇰 Official Bot\n\n★彡 ʙᴏᴛ ʙʏ 彡★\n[◤ᴵᴬᴹǤΐรhaή ᴷʳⁱˢʰᵏᵃ◢ 『🇱🇰』](https://t.me/Imgishan)\n[unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™](t.me/UnknownB_o_y)"
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_message(filters.command(["help", "help@MemeHubTgSl_Bot"]))
async def help(bot, message):
    if force_subchannel:
        try:
            user = await bot.get_chat_member(force_subchannel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Yourt Banned")
                return 
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            await bot.send_sticker(message.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await message.reply_text(
            text=text,
            reply_markup=reply_markup
            ) 
            return
    await bot.send_sticker(message.chat.id, random.choice(HELP_STICKER), reply_markup=REPLY_BUTTONS)
    await message.reply_text(
        text=HELP_STRING,
        reply_markup=CLOSE_BUTTON,
        disable_web_page_preview=True
         )

                       
print("cmds.py Working....")








