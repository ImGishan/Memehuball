import os
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from .config import force_subchannel, FORCESUB_TEXT, FORCESUB_BUTTONS, HELP_STRING, CLOSE_BUTTON, HELP_STICKER
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel

@Client.on_message(filters.command(["help", "help@MemeHubTgSl_Bot"]))
async def startprivate(bot, message):
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
    await bot.send_sticker(message.chat.id, random.choice(HELP_STICKER))
    await message.reply_text(
        text=HELP_STRING,
        reply_markup=CLOSE_BUTTON,
        disable_web_page_preview=True
         )
         
         
print("Help Working....")