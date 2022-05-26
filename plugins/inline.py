import os
from pyrogram import Client, filters
from pyrogram.types import *
from .config import *
from pyrogram.types import (Message, InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, ReplyKeyboardMarkup, InlineQueryResultVideo)
                            

@Client.on_inline_query()
async def answer(client, inline_query):
   if inline_query.query=='share':
        await inline_query.answer(
            results=[
                InlineQueryResultVideo(
                    title="Share Karapam",
                    video_url="https://telegra.ph/file/81e48822088894ee0b425.mp4",
                    thumb_url="https://telegra.ph/file/7c8846dcae3767b15e3c0.jpg",
                    caption="""
𝙷𝚒. 𝙱𝚘𝚢𝚜 𝚊𝚗𝚍 𝚐𝚒𝚛𝚕𝚜 𝚠𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚖𝚎𝚖𝚎𝚑𝚞𝚋 𝚒𝚏 𝚢𝚘𝚞 𝚑𝚊𝚟𝚎 𝚖𝚎𝚖𝚎𝚜 𝚜𝚎𝚗𝚍 𝚢𝚘𝚞𝚛 𝚖𝚎𝚖𝚎𝚜 𝚝𝚘 𝚘𝚞𝚛 𝚋𝚘𝚝 𝚊𝚗𝚍 𝚑𝚎𝚕𝚙 𝚞𝚜.
𝙼𝚎𝚖𝚎𝚑𝚞𝚋 එකේ ඇඩ්මින් නැ කියල දුකෙම්ද ඉන්නේ 𝚖𝚎𝚖𝚎𝚜 ගොඩගැහිලා ඒවාට කරගන්න දෙයක් නේද? මෙන්න විසදුම ඔයාගේ 𝚖𝚎𝚖𝚎𝚜/𝚏𝚞𝚗𝚗𝚢 𝚟𝚒𝚍𝚎𝚘𝚜 ඔක්කොම එවන්න අපිට අපි ඒවා දානවා අපේ 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 එකේ ඒ අතරින් හැමදාම 𝚖𝚎𝚖𝚜 දාන අයට අපේ 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 එකේ ඇඩ්මින් වෙන්නත් පුළුවන් අදම එක්වන්න අප සමග 🤞✌️🤟🤘👊
𝙱𝚘𝚝 = @MemehubTgSl_Bot
""",
                    reply_markup=InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton('🐞 Report Bugs 🐞', user_id="1884885842")
                 ],
                 [
                 InlineKeyboardButton('ᴍᴇᴍᴇʜᴜʙ ᴏᴍғғɪᴄɪᴀʟ ʙᴏᴍᴛ 『🇱🇰』', user_id="@MemeHubTgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share")
                 ]])
                    
                        
                     
            ),
            ],
            cache_time=1
        ) 