# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
import os
import time
import math
import aiohttp
import aiofiles
from pyrogram.errors import MessageNotModified
from helper_funcs.display_progress import humanbytes, TimeFormatter

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def DetectFileSize(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return int(response.headers.get("content-length", 0))
    except:
        return 0


async def DownLoadFile(url, file_name, chunk_size, client, ud_type, message_id, chat_id):
    if os.path.exists(file_name):
        os.remove(file_name)
    if not url:
        return file_name
        
    start_time = time.time()
    downloaded_size = 0
    
    # Fast async download so the bot doesn't freeze for other users
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            total_size = int(response.headers.get("content-length", 0))
            
            async with aiofiles.open(file_name, 'wb') as fd:
                async for chunk in response.content.iter_chunked(chunk_size):
                    if chunk:
                        await fd.write(chunk)
                        downloaded_size += len(chunk)
                        
                        now = time.time()
                        diff = now - start_time
                        
                        # Update animation every 5 seconds 
                        if round(diff % 5.00) == 0 or downloaded_size == total_size:
                            try:
                                percentage = downloaded_size * 100 / total_size if total_size else 0
                                speed = downloaded_size / diff if diff else 1
                                
                                elapsed_time = round(diff) * 1000
                                time_to_completion = round((total_size - downloaded_size) / speed) * 1000 if speed else 0
                                estimated_total_time = elapsed_time + time_to_completion

                                estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
                                
                                # 🌟 Advance Premium Progress Bar 🌟
                                progress_filled = ''.join(["⬢" for i in range(math.floor(percentage / 5))])
                                progress_empty = ''.join(["⬡" for i in range(20 - math.floor(percentage / 5))])
                                progress_bar = f"[{progress_filled}{progress_empty}]"

                                tmp = (
                                    f"{progress_bar}\n\n"
                                    f"🚀 **ᴘʀᴏɢʀᴇss:** `{round(percentage, 2)}%`\n"
                                    f"💾 **sɪᴢᴇ:** `{humanbytes(downloaded_size)} ᴏғ {humanbytes(total_size)}`\n"
                                    f"⚡ **sᴘᴇᴇᴅ:** `{humanbytes(speed)}/s`\n"
                                    f"⏳ **ᴇᴛᴀ:** `{estimated_total_time if estimated_total_time != '' else '0 s'}`\n"
                                )
                                
                                # Fixed Pyrogram V2 Edit Message Function
                                await client.edit_message_text(
                                    chat_id,
                                    message_id,
                                    text=f"**{ud_type}**\n\n{tmp}"
                                )
                            except MessageNotModified:
                                pass
                            except Exception as e:
                                pass
    return file_name
