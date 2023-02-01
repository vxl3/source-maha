## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCNXsJ4VWxUanK-HoUoOI4W_Tw5t8zbEBHnQzG0qMqOQ75OADD6GMLpLFyqLFnKrEkw3PYMaFy46YaA-w3GV78FTWTKztdpJ47qZ2nNn5YrUpmW8LVCVRJZ21nXaAgE8moO7iGGcdpflCIIwD8KiLDos-kncAgGG9JK6L6bKv0Iir_MUggJtDa5u99LbGfo1c8BtQsMXdE84_k0YoexvRuLe0VGP5xL2iKCRyl-DeTOM5nkr0MYb6bhI9ha9sdelt39HBSKeYS1YnNk9yPHgbB0hcozrB-2VKLBwAZNOJ-yUmpBfdsd2me1eW6pWjmDWlQHxlMZQq5zGiyAl-iQKR5TAAAAAVH1mDMA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "29699592"))
API_HASH = getenv("API_HASH", "36c5d87a0d72b145a014b89def282cbd")
OWNER_NAME = getenv("OWNER_NAME", "DENAR")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
BOT_IMG = getenv("BOT_IMG")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "IS0IX")
BOT_USERNAME = getenv("BOT_USERNAME", "D3NARBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "D3NAR")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "XI_I0")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/66d20566acacf826372d7.jpg")
