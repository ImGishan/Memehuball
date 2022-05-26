import os
from pyrogram import Client, filters
from pyrogram.types import *
from .config import CALCULATE_TEXT, CALCULATE_BUTTONS

@Client.on_message(filters.command(["calc", "calculate", "calculator"]))
async def calculate(bot, update):
    await update.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
    

print("Cal Working....")   