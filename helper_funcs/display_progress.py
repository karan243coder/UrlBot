
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import math, os, time, shutil

from config import Config
from translation import Translation
from pyrogram.errors import MessageNotModified

async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    
    # Updated to 5.00 seconds for smoother and faster progress bar animation
    if round(diff % 5.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        # 🌟 Advance Premium Progress Bar Design 🌟
        progress_filled = ''.join(["⬢" for i in range(math.floor(percentage / 5))])
        progress_empty = ''.join(["⬡" for i in range(20 - math.floor(percentage / 5))])
        progress_bar = f"[{progress_filled}{progress_empty}]"

        tmp = (
            f"{progress_bar}\n\n"
            f"🚀 **ᴘʀᴏɢʀᴇss:** `{round(percentage, 2)}%`\n"
            f"💾 **sɪᴢᴇ:** `{humanbytes(current)} ᴏғ {humanbytes(total)}`\n"
            f"⚡ **sᴘᴇᴇᴅ:** `{humanbytes(speed)}/s`\n"
            f"⏳ **ᴇᴛᴀ:** `{estimated_total_time if estimated_total_time != '' else '0 s'}`\n"
        )

        try:
            await message.edit(
                text=f"**{ud_type}**\n\n{tmp}"
            )
        except MessageNotModified:
            pass
        except Exception as e:
            pass

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]
