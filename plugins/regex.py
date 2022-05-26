import os
import random
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from .config import *

@Client.on_message(filters.private & filters.regex(pattern="🤴 OWNER 🤴"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(OWNER_STICKER),reply_markup=OWNER_BTN
     )
@Client.on_message(filters.private & filters.regex(pattern="💻 Bot Devs 💻"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(DEV_STICKER),reply_markup=DEV_BTN
     )

@Client.on_message(filters.private & filters.regex(pattern="👮‍♂️ MemeHub Admins 👮‍♂️"))   
async def startprivate(bot, message):
     await bot.send_sticker(message.chat.id, random.choice(ADMIN_STICKER),reply_markup=ADMIN_BTN
     )
    
@Client.on_message(filters.private & filters.regex(pattern="NEXT 🔜"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='NEXT 🔜',reply_markup=NEXT_1
     )
        
@Client.on_message(filters.private & filters.regex(pattern="BACK 🔙"))   
async def startprivate(bot, message):
     await bot.send_message(message.chat.id, text='BACK 🔙',reply_markup=REPLY_BTN
     )
