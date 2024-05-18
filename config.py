import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26950524")

API_HASH = os.environ.get("API_HASH", "f4fb3d1cd320a027837830c89d70d506")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7123659411:AAE7vwTEKCEDTrtxL65VDxCXLrvrynhisdQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "1002081316321.") 

DB_NAME = os.environ.get("DB_NAME","MONGODB")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://akvvetha:2640@cluster0.htdlwze.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5616093790.').split()]

PORT = os.environ.get("PORT", "8080")
