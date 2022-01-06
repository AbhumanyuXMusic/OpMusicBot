import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Dr_Asad_Ali")
ALIVE_NAME = getenv("ALIVE_NAME", "Asad Ali")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Shayri_Music_Lovers")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsadSupport")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/de138de8fd880becb9cf1.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AbhumanyuXMusic/OpMusicBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/006da7a40b81bd6cb2840.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/006da7a40b81bd6cb2840.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/006da7a40b81bd6cb2840.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/006da7a40b81bd6cb2840.png")

# Don't Change It Bro ❣️ 😂


MY_SERVER = getenv("MY_SERVER", "AlishaSupport")
REPO_OWNER = getenv("REPO_OWNER", "Itz_VeNom_xD")
MY_HEART = getenv("MY_HEART", "candy_626")
BOT_UPDATE = getenv("BOT_UPDATE", "Shayri_Music_Lovers")
MY_BRO = getenv("MY_BRO", "HarshitSharma361")
