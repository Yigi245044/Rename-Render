# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21037450")

API_HASH = os.environ.get("API_HASH", "05ac9eb7c523b83c51d89d1f2f91d58b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6686737285:AAFS95C2rwkYtwC-dipW2ePCSTJTTiXxG5Y") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "AniME_YoGi_LovEr")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://AniME_YoGi_LovEr:AniME_YoGi_LovEr@cluster0.bbisgsh.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/5d43f3a878ff1f428a634.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
