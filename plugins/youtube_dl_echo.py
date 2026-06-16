# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging, requests, os, asyncio, json
from config import Config
from pyrogram import filters, enums, Client
from database.adduser import AddUser
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper_funcs.display_progress import humanbytes

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & ~filters.via_bot & filters.regex(pattern=".*http.*"))
async def echo(bot, update):
    await AddUser(bot, update)
    imog = await update.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴅᴇᴀʀ...⚡**", reply_to_message_id=update.id)
    
    # Log channel notification
    if Config.TECH_VJ_LOG_CHANNEL:
        try:
            await bot.send_message(
                chat_id=Config.TECH_VJ_LOG_CHANNEL, 
                text=f"**#NEW_LINK** 📥\n\n👤 **User:** {update.from_user.mention}\n🔗 **Link:** `{update.text}`"
            )
        except Exception as e:
            logger.warning(f"Log Error: {e}")

    url = update.text
    command_to_exec = ["yt-dlp", "--no-warnings", "--youtube-skip-dash-manifest", "-j", url]
        
    process = await asyncio.create_subprocess_exec(*command_to_exec,
    stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    t_response = stdout.decode().strip()
    
    if t_response:
        response_json = json.loads(t_response.split('\n')[0])
        save_ytdl_json_path = f"{Config.TECH_VJ_DOWNLOAD_LOCATION}/{update.from_user.id}.json"
        with open(save_ytdl_json_path, "w", encoding="utf8") as outfile:
            json.dump(response_json, outfile, ensure_ascii=False)
            
        inline_keyboard = []
        if "formats" in response_json:
            for formats in response_json["formats"]:
                format_id = formats.get("format_id")
                format_ext = formats.get("ext")
                format_note = formats.get("format_note", "best")
                approx_file_size = humanbytes(formats.get("filesize", 0))
                
                cb_data = f"video|{format_id}|{format_ext}"
                inline_keyboard.append([
                    InlineKeyboardButton(f"S {format_note} ({approx_file_size})", callback_data=cb_data.encode("UTF-8"))
                ])
        
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        await imog.delete()
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.TECH_VJ_FORMAT_SELECTION,
            reply_markup=reply_markup,
            reply_to_message_id=update.id
        )
    else:
        await imog.delete()
        await update.reply_text("❌ **Invalid URL or no formats found.**")
