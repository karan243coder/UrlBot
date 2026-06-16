# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    TECH_VJ_BOT_TOKEN = os.environ.get("TECH_VJ_BOT_TOKEN", ":-ukHag0us")
    TECH_VJ_BOT_USERNAME = os.environ.get("TECH_VJ_BOT_USERNAME", " ") # Bot username without @.
    
    # The Telegram API things
    TECH_VJ_API_ID = int(os.environ.get("TECH_VJ_API_ID", "23171051"))
    TECH_VJ_API_HASH = os.environ.get("TECH_VJ_API_HASH", "10331d5d712364f57ffdd23417f4513c")
    
    # the download location, where the HTTP Server runs
    TECH_VJ_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    TECH_VJ_MAX_FILE_SIZE = 50000000
    TECH_VJ_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    TECH_VJ_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    TECH_VJ_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    TECH_VJ_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    TECH_VJ_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    TECH_VJ_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    TECH_VJ_OWNER_ID = int(os.environ.get("TECH_VJ_OWNER_ID", "5071005351")) 
    TECH_VJ_SESSION_NAME = "Cluster0"
    
    # database uri (mongodb)
    TECH_VJ_DATABASE_URL = os.environ.get("TECH_VJ_DATABASE_URL", "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    TECH_VJ_MAX_RESULTS = "50"

    # channel information
    # 🔴 DHYAN RAHE: Niche "-1002367641884" ki jagah apne Log Channel ka ID daalna hai
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "-1002367641884")) 
    
    # if you want force subscribe then give your channel id below else leave blank
    tech_vj_update_channel = environ.get('TECH_VJ_UPDATES_CHANNEL', '') 
    TECH_VJ_UPDATES_CHANNEL = int(tech_vj_update_channel) if tech_vj_update_channel and id_pattern.search(tech_vj_update_channel) else None  
    
    # Url Shortner Information 
    TECH_VJ = bool(environ.get('TECH_VJ', False)) # Set False If you want shortlink off else True
    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'modijiurl.com') 
    TECH_VJ_API = environ.get('TECH_VJ_API','1f0a7d7bf27a040bf0cebbaaa6478c1f7f0ba46a') 
    TECH_VJ_TUTORIAL = os.environ.get("TECH_VJ_TUTORIAL", "https://t.me/How_To_Open_Linkl")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
