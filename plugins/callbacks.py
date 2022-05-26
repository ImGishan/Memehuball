from pyrogram import Client, filters
from pyrogram.types import *
from .config import *

@Client.on_callback_query()
async def cb_data(bot, update):
        data = update.data
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            message_text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await update.message.edit_text(
                text=f"{text}\n\n{CALCULATE_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon.....",
        )
    elif update.data == "bak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʙᴀᴍᴄᴋ 👻",
         )
    elif update.data == "bak":
         await update.message.delete()
         await bot.delete_message(update.chat.id, update.message.id)
    elif update.data == "hlp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=CLOSE_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʜᴇᴍʟᴘ 👻",
         )
    elif update.data == "cloce":
         await update.message.delete()
    elif update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
        ) 
