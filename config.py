## What's up Kangers

import os

from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):

    load_dotenv("local.env")

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "Abdulrahman")

BOT_TOKEN = getenv("BOT_TOKEN", "5913213329:AAHD4d7ER1w_7SdnVeXb1tfnIxDCndoAz9k")

BOT_NAME = getenv("BOT_NAME", "test")

API_ID = int(getenv("API_ID", "11224923"))

API_HASH = getenv("API_HASH", "ba8f4ea9c780a7ba160a928c8d433191")

OWNER_NAME = getenv("OWNER_NAME", "MR_X")

OWNER_USERNAME = getenv("OWNER_USERNAME", "MR_X_N")

ALIVE_NAME = getenv("ALIVE_NAME", "MR_X")

BOT_USERNAME = getenv("BOT_USERNAME", "test0X7bot")

OWNER_ID = getenv("OWNER_ID", "5443938270")

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MR_X")

GROUP_SUPPORT = getenv("GROUP_SUPPORT", "test15tt")

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "test15t")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5443938270").split()))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/3f3dc7b3ac92a0fec3402.jpg")

START_PIC = getenv("START_PIC", "https://telegra.ph/file/0bbed3746b379ca414982.jpg")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Abdulrahmman8894/Zaid-Vc-Player")

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/cdd58e46c0dad030d5875.jpg")

IMG_2 = getenv("IMG_2", "https://telegra.ph/file/22f3c2b3e9757e9c0e1a3.jpg")

IMG_3 = getenv("IMG_3", "https://telegra.ph/file/22f3c2b3e9757e9c0e1a3.jpg")

IMG_4 = getenv("IMG_4", "https://telegra.ph/file/22f3c2b3e9757e9c0e1a3.jpg")

IMG_5 = getenv("IMG_5", "https://telegra.ph/file/22f3c2b3e9757e9c0e1a3.jpg")

IMG_6 = getenv("IMG_6", "https://telegra.ph/file/22f3c2b3e9757e9c0e1a3.jpg")

