import logging

from pyrogram import Client, idle

logging.getLogger("pyrogram").setLevel(logging.INFO)

#Client
Client = Client(
    "Memehub Bot",
    
    api_id= 8838171,
    api_hash= "0587408d4f7d9301f5295840b0f3b494",
    bot_token= "5011377446:AAHavxAS4fO42B41mNVcKVoQL8z6D6_LUdU",
    plugins=dict(root="plugins"),
)


Client.start()
uname = (Client.get_me()).username
print(f"@{uname} Deployed Successfully !")

idle()


