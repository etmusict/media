

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "MediaToTelegraphLink",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
ุงููุง {message.from_user.mention},
๐ฎุฃูุง ููุง ูุฅูุดุงุก ุฑูุงุจุท ุงูุชูุฌุฑุงู ููููุงุช ุงููุณุงุฆุท ุงูุฎุงุตุฉ ุจู.

๐จ๐ผโ๐ปูุง ุนููู ุณูู ุฅุฑุณุงู ููู ูุณุงุฆุท ุตุงูุญ ูุจุงุดุฑุฉ ุฅูู ูุฐู ุงูุฏุฑุฏุดุฉ.
โป๏ธุงููุงุน ุงููููุงุช ุงูุตุงูุญู ูู:- 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

๐ูุฃูุดุงุก ุงูุฑูุงุจุท ูู **ุงููุฌููุนุงุช**,ุงุถููู ููุฌููุนู ุฎุงุฑูู ุงู ุนุงูู ูุงุฑุณู ุงูุงูุฑ <code>/tl</code> ุฑุฏุง ุนูู ููู ูุณุงุฆุท ุตุงูุญ.
๐ฅ | [๐บ๐ถ๐ผ๐น๐ช๐ฌ ๐ฝ๐จ๐ด๐ฉ๐ฐ๐น๐](https://t.me/XxvprxX)

โฃ๏ธ | [แฏหน ๐๐ผ๐๐ฝ๐๐๐ฃฅโโโโโ๐ต๐ธูููุจูููุฑูอข๏ผโง](https://t.me/XxlllllllllllllllllllllllllllxX)
            """
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("๐ฎุงูุชุธุฑ ููููุง...")
        async def progress(current, total):
            await text.edit_text(f"๐ฅ ุฌุงุฑู ุงูุชูุฒูู... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("๐ค ุฌุงุฑู ุงูุฑูุน ุงูู ุงูุชููุฌุฑุงู...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**๐ | ุฑุงุจุท ุงูุชููุฌุฑุงู**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**โ | ูุดู ุฑูุน ุงูููู**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("๐ฎุงูุชุธุฑ ููููุง...")
        async def progress(current, total):
            await text.edit_text(f"๐ฅ ุฌุงุฑู ุงูุชูุฒูู... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("๐ค ุฌุงุฑู ุงูุฑูุน ุงูู ุงูุชููุฌุฑุงู...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**๐ | ุฑุงุจุท ุงูุชููุฌุฑุงู**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**โ | ูุดู ุฑูุน ุงูููู**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("ุงูุจูุช ุดุบุงู!")
teletips.run()

