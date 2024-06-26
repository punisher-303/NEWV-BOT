from pyrogram import Client, filters 
from info import ADMINS, DOWNLOAD_LOCATION
import os

dir = os.listdir(DOWNLOAD_LOCATION)

# dir = "./DOWNLOADS"

@Client.on_message(filters.command("setthumb") & filters.private & filters.photo & filters.user(ADMINS))                            
async def set_tumb(bot, msg):       
    if len(dir) == 0:
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        return await msg.reply(f"Your permanent thumbnail is saved in dictionary ✅️ \nif you change yur server or recreate the server app to again reset your thumbnail⚠️")            
    else:    
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")               
        return await msg.reply(f"Your permanent thumbnail is saved in dictionary ✅️ \nif you change yur server or recreate the server app to again reset your thumbnail⚠️")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMINS))                            
async def view_tumb(bot, msg):
    try:
        await msg.reply_photo(photo=f"{DOWNLOAD_LOCATION}/thumbnail.jpg", caption="this is your current thumbnail")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="you don't have any thumbnail")

@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMINS))                            
async def del_tumb(bot, msg):
    try:
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await msg.reply_text("your thumbnail was removed🚫")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="you don't have any thumbnail")
    
