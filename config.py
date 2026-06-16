# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # Bot Information 
    # Yahan apna Token daalo, jaise: "123456:ABC-DEF1234..."
    TECH_VJ_BOT_TOKEN = os.environ.get("TECH_VJ_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    
    # Yahan bot ka username bina @ ke daalo
    TECH_VJ_BOT_USERNAME = os.environ.get("TECH_VJ_BOT_USERNAME", "Lisafans_bot")
    
    # The Telegram API things
    TECH_VJ_API_ID = int(os.environ.get("TECH_VJ_API_ID", "23171051"))
    TECH_VJ_API_HASH = os.environ.get("TECH_VJ_API_HASH", "10331d5d712364f57ffdd23417f4513c")
    
    # Download location
    TECH_VJ_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram max file upload size
    TECH_VJ_MAX_FILE_SIZE = 50000000
    TECH_VJ_TG_MAX_FILE_SIZE = 4194304000
    TECH_VJ_FREE_USER_MAX_FILE_SIZE = 50000000
    
    TECH_VJ_CHUNK_SIZE = int(128)
    TECH_VJ_HTTP_PROXY = ""
    TECH_VJ_MAX_MESSAGE_LENGTH = 4096
    TECH_VJ_PROCESS_MAX_TIMEOUT = 3600
    
    # Owner ID and Session
    TECH_VJ_OWNER_ID = int(os.environ.get("TECH_VJ_OWNER_ID", "5071005351")) 
    TECH_VJ_SESSION_NAME = "Lisafans_bot"
    
    # Database URI (Use the link we finalized)
    TECH_VJ_DATABASE_URL = os.environ.get("TECH_VJ_DATABASE_URL", "mongodb+srv://karan:Karan1234@cluster0.cnecz4s.mongodb.net/?appName=Cluster0")
    TECH_VJ_MAX_RESULTS = "50"

    # Channel ID
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "-1002367641884")) 
    
    tech_vj_update_channel = environ.get('TECH_VJ_UPDATES_CHANNEL', '') 
    TECH_VJ_UPDATES_CHANNEL = int(tech_vj_update_channel) if tech_vj_update_channel and id_pattern.search(tech_vj_update_channel) else None  
    
    # Url Shortner Information 
    TECH_VJ = False # Shortlink OFF rakhna better hai start mein
    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'modijiurl.com') 
    TECH_VJ_API = environ.get('TECH_VJ_API', '1f0a7d7bf27a040bf0cebbaaa6478c1f7f0ba46a') 
    TECH_VJ_TUTORIAL = os.environ.get("TECH_VJ_TUTORIAL", "https://t.me/How_To_Open_Linkl")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
