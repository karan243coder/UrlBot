from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    TECH_VJ_START_TEXT = """
<b>ʜᴇʟʟᴏ {} 👋

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀᴅᴠᴀɴᴄᴇ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ

ɢɪᴠᴇ ᴍᴇ ᴀɴʏ ʟɪɴᴋ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪɴᴛᴏ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ

ᴛʜɪs ʙᴏᴛ ɪs ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href="https://t.me/botio_devs">.𝖎𝖔 𝖉𝖊𝖛𝖘</a></b>
"""

    TECH_VJ_HELP_TEXT = """
<b>🖍️ ғᴇᴀᴛᴜʀᴇs :-

🔺 ᴜᴘʟᴏᴀᴅ <a href="https://t.me/VJCode/4">ʏᴛ-ᴅʟᴘ sᴜᴘᴘᴏʀᴛᴇᴅ ʟɪɴᴋs</a> ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ.

🔺 ᴜᴘʟᴏᴀᴅ ʜᴛᴛᴘ/ʜᴛᴛᴘs ᴀs ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ.

🔺 ᴜᴘʟᴏᴀᴅ ᴢᴇᴇ5, sᴏɴʏ.ʟɪᴠᴇ, ᴠᴏᴏᴛ ᴀɴᴅ ᴍᴜᴄʜ ᴍᴏʀᴇ.

🔺 ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ.

🔺 ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ʙʏ /broadcast ᴄᴏᴍᴍᴀɴᴅ

💢 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ :-

🔻 ʜᴏᴡ ᴛᴏ ᴜᴘʟᴏᴀᴅ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋs <a href="https://t.me/VJCode/11">ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ</a>

🔻 sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɢᴏᴏɢʟᴇ ᴅʀɪᴠᴇ | ʏᴛᴅʟ | ᴅɪʀᴇᴄᴛ ʟɪɴᴋs.

🔻sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴏᴘᴛɪᴏɴ.

🔻 ᴛʜᴇɴ ʙᴇ ʀᴇʟᴀxᴇᴅ ʏᴏᴜʀ ғɪʟᴇ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ sᴏᴏɴ..</b> 
"""

    TECH_VJ_ABOUT_TEXT = """
<b>♻️ ᴍʏ ɴᴀᴍᴇ : ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ

🌀 ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/botio_devs">ᴠᴊ ʙᴏᴛᴢ</a>

🌺 ʜᴇʀᴏᴋᴜ : <a href="https://heroku.com/">ʜᴇʀᴏᴋᴜ</a>

📑 ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ 3.10.5</a>

🇵🇲 ғʀᴀᴍᴇᴡᴏʀᴋ : <a href="https://docs.pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ 2.0.30</a>

👲 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href="https://t.me/APPUZ_001">ᴀᴘᴘᴜꜱ</a></b>

"""

    
    TECH_VJ_START_BUTTONS = InlineKeyboardMarkup(
        [ [
            InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/botio_devs')
        ],[
            InlineKeyboardButton('❓ ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🦊 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('🇮🇳 ғᴏʟʟᴏᴡ ᴍᴇ ᴏɴ ɪɴsᴛᴀɢʀᴀᴍ 💖', url='https://www.instagram.com/______jisto__?igsh=NjVtaDV2b2dqZTMy')
        ]]
    )
    TECH_VJ_HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/botio_devs')
        ], [
            InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('🦊 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('📛 ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    TECH_VJ_ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/botio_devs')
        ], [
            InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('❓ ʜᴇʟᴘ', callback_data='help')
        ], [
            InlineKeyboardButton('📛 ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    
    TECH_VJ_ERROR = "<b>ᴇʀʀᴏʀ : {}</b>"

    
    TECH_VJ_FORMAT_SELECTION = "<b>ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ғᴏʀᴍᴀᴛ: ғɪʟᴇ ꜱɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ \nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇғᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀғᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏғ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ.\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ.</b>"
    TECH_VJ_SET_CUSTOM_USERNAME_PASSWORD = """<b>Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴅᴇᴏꜱ, ᴘʀᴏᴠɪᴅᴇ ɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ғᴏʀᴍᴀᴛ:\nURL | ғɪʟᴇɴᴀᴍᴇ | ᴜꜱᴇʀɴᴀᴍᴇ | ᴘᴀꜱꜱᴡᴏʀᴅ</b>"""
    TECH_VJ_DOWNLOAD_START = "<b>📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>"
    TECH_VJ_UPLOAD_START = "<b>📤 ᴜᴘʟᴏᴀᴅɪɴɢ...</b>"
    TECH_VJ_RCHD_TG_API_LIMIT = "<b>ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ.\nᴅᴇᴛᴇᴄᴛᴇᴅ ғɪʟᴇ ꜱɪᴢᴇ: {}\nꜱᴏʀʀʏ. ʙᴜᴛ, ɪ ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇꜱ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 𝟸GB ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ API ʟɪᴍɪᴛᴀᴛɪᴏɴꜱ.</b>"
    TECH_VJ_AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>ᴛʜᴀɴᴋꜱ ғᴏʀ ᴜꜱɪɴɢ ᴍᴇ\n\nJᴏɪɴ : https://t.me/botio_devs</b>"
    TECH_VJ_AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "<b>ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ.\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ.\n\nhttps://t.me/botio_devs</b>"
    TECH_VJ_SAVED_CUSTOM_THUMB_NAIL = "<b>ᴄᴜꜱᴛᴏᴍ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ. Tʜɪꜱ ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ғɪʟᴇ.</b>"
    TECH_VJ_DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ ꜱᴜᴄᴄᴇꜱғᴜʟʟʏ.</b>"
    TECH_VJ_CUSTOM_CAPTION_UL_FILE = "<b>{}</b>"
    TECH_VJ_NO_VOID_FORMAT_FOUND = "<b>ᴇʀʀᴏʀ...\nTᴇᴄʜ VJ ꜱᴀɪᴅ: {}</b>"
    TECH_VJ_REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>ʀᴇᴘʟʏ /generatecustomthumbnail ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ, ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙᴀɪʟ</b>"
    TECH_VJ_ERR_ONLY_TWO_MEDIA_IN_ALBUM = """<b>ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ ꜱʜᴏᴜʟᴅ ᴄᴏɴᴛᴀɪɴ ᴏɴʟʏ ᴛᴡᴏ ᴘʜᴏᴛᴏꜱ. ᴘʟᴇᴀꜱᴇ ʀᴇ-ꜱᴇɴᴅ ᴛʜᴇ ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ, ᴀɴᴅ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ, ᴏʀ ꜱᴇɴᴅ ᴏɴʟʏ ᴛᴡᴏ ᴘʜᴏᴛᴏꜱ ɪɴ ᴀɴ ᴀʟʙᴜᴍ.\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ /ʀᴇɴᴀᴍᴇ ᴄᴏᴍᴍᴀɴᴅ ᴀғᴛᴇʀ ʀᴇᴄᴇɪᴠɪɴɢ ғɪʟᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ ᴡɪᴛʜ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴜᴘᴘᴏʀᴛ.</b>"""
    TECH_VJ_CANCEL_STR = "<b>ᴘʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟʟᴇᴅ</b>"
    TECH_VJ_ZIP_UPLOADED_STR = "<b>ᴜᴘʟᴏᴀᴅᴇᴅ {} ғɪʟᴇꜱ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ</b>"
    TECH_VJ_SLOW_URL_DECED = "<b>Gᴏꜱʜ ᴛʜᴀᴛ ꜱᴇᴇᴍꜱ ᴛᴏ ʙᴇ ᴀ ᴠᴇʀʏ ꜱʟᴏᴡ URL. Sɪɴᴄᴇ ʏᴏᴜ ᴡᴇʀᴇ ꜱᴄʀᴇᴡɪɴɢ ᴍʏ ʜᴏᴍᴇ, I ᴀᴍ ɪɴ ɴᴏ ᴍᴏᴏᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜɪꜱ ғɪʟᴇ. ᴍᴇ ᴀ ғᴀꜱᴛ URL ꜱᴏ ᴛʜᴀᴛ I ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ, ᴡɪᴛʜᴏᴜᴛ ᴍᴇ ꜱʟᴏᴡɪɴɢ ᴅᴏᴡɴ ғᴏʀ ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ.</b>"

    TECH_VJ_ERROR_YTDLP = "<b>ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ᴛʜɪꜱ ɪꜱꜱᴜᴇ ᴏɴ https://yt-dl.org/bug . ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴛʜᴇ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ; ꜱᴇᴇ  https://yt-dl.org/update ᴏɴ ʜᴏᴡ ᴛᴏ ᴜᴘᴅᴀᴛᴇ. ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴄᴀʟʟ ʏᴏᴜᴛᴜʙᴇ-ᴅʟ ᴡɪᴛʜ ᴛʜᴇ --ᴠᴇʀʙᴏꜱᴇ ғʟᴀɢ ᴀɴᴅ ɪɴᴄʟᴜᴅᴇ ɪᴛꜱ ᴄᴏᴍᴘʟᴇᴛᴇ ᴏᴜᴛᴘᴜᴛ.</b>"



# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from config import Config
from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from pyrogram import Client as Tech_VJ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from plugins.forcesub import get_invite_link

@Tech_VJ.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
          await update.message.delete(True)


@Tech_VJ.on_callback_query()
async def button(bot, update):
    if "|" in update.data:
        await youtube_dl_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)

    elif update.data == "home":
        await update.message.edit(
            text=Translation.TECH_VJ_START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.TECH_VJ_START_BUTTONS,
            # disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit(
            text=Translation.TECH_VJ_HELP_TEXT,
            reply_markup=Translation.TECH_VJ_HELP_BUTTONS,
            # disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit(
            text=Translation.TECH_VJ_ABOUT_TEXT,
            reply_markup=Translation.TECH_VJ_ABOUT_BUTTONS,
            # disable_web_page_preview=True
        )
    elif "close" in update.data:
        await update.message.delete(True)

    elif "refreshForceSub" in update.data:
        if Config.TECH_VJ_UPDATES_CHANNEL:
            if str(Config.TECH_VJ_UPDATES_CHANNEL).startswith("-100"):
                channel_chat_id = int(Config.TECH_VJ_UPDATES_CHANNEL)
            else:
                channel_chat_id = Config.TECH_VJ_UPDATES_CHANNEL
            try:
                user = await bot.get_chat_member(channel_chat_id, update.message.chat.id)
                if user.status == "kicked":
                    await update.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [owner](https://t.me/kingvj01).",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                chat_id = channel_chat_id
                invite_link = await get_invite_link(bot, chat_id)
                await update.message.edit(
                    text="**I like Your Smartness But Don't Be Oversmart! 😑**\n\n",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshForceSub")
                            ]
                        ]
                    )
                )
                return
            except Exception:
                await update.message.edit(
                    text="Something went Wrong. Contact my [owner](https://t.me/kingvj01).",
                    disable_web_page_preview=True
                )
                return
        await update.message.edit(
            text=Translation.TECH_VJ_START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.TECH_VJ_START_BUTTONS,
            disable_web_page_preview=True
    )
