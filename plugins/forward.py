import os
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from .config import force_subchannel, FORCESUB_TEXT, FORCESUB_BUTTONS, BACK_BUTTONS, force_subchannel, FORCESUB_TEXT, FORCESUB_BUTTONS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
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
    if message.from_user.id == 1884885842:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=1884885842,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {info.first_name}\n\n{message.text}**"
    )
    await bot.send_message(
        chat_id=-1001581011760,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> {message.from_user.mention}\n\n{message.text}**"
    )
    
@Client.on_message(filters.media & filters.private)
async def pm_media(bot, message):
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
    if message.from_user.id == 1884885842:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await message.forward(1884885842)
    
    await bot.send_message(1884885842 ,f"Photo from:</b> {reference_id} **\n**Name:</b> {info.first_name}")
    await message.forward(-1001210985373)
    await message.forward(-1001759991131)
    await bot.send_message(
        chat_id=-1001759991131,
        text=f"**Msg from:</b> {reference_id} **\n**Name:</b> [{message.from_user.first_name}](tg://user?id={message.from_user.id})**\n\n@admin"
    )
    reply_markup = BACK_BUTTONS
    text = "Ur Photo Sent To [MemeHub Telegram 🇱🇰](https://t.me/memehubTGSL)"
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    
@Client.on_message(filters.sticker & filters.private) 
async def pm_media(bot, message):
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
    file_id = "CAADBQADEwUAAmjn4Vez7jrL1Cu2AAEC"
    await bot.send_sticker(message.chat.id, file_id) 

@Client.on_message(filters.text)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        ) 
        
@Client.on_message(filters.user(1884885842) & filters.media)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )             
        
print("Pm Working....")