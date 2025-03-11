import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "26926782"))
API_HASH = os.environ.get("API_HASH", "9b2fac908fb7f9a3dabac3b0a57211b1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7786105206:AAHm0iceXktLQugF_5xs-lRj8xjbtMR-xE0")
ADMIN = int(os.environ.get("ADMIN", "1214167849"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "Movie_Centre1")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002354465117"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Utkarsh123:9335924360@utkarsh9.af91n.mongodb.net/?retryWrites=true&w=majority&appName=Utkarsh9")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "hakshsgs")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
