import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "11480225"))
API_HASH = getenv("API_HASH", "4e246bace68111a0d82fa2ce96e0e5e3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6981145147:AAHdUgH5p3_KHJJ9ClWF7u-WCDpJix5O8G0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://nahmedofh:<password>@cluster0.ixptgtm.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001952936217"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6951022833"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Theferid/The_ferid",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FerooResmi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GunelSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgAo4v3kDyub-q6GLzFLSZS5Q99iCeKS1ybMp4WkpEg5cqi3uUvAhByNARkfp7OBWQBBU5g3WLpPfKa_HnAp2SI9jqSW1Xud-4NX1d6WYaQs5bkyuw-1vrsP1qBvIx-SdCq6Mo-PVNXLNYAhs4pDTAdICBfPFQvdmsx4rmXuRQOl1QqppmzeYKLe4ZAq0kJq3qodV0S4M7LHk8q8Y7HwiHhvgx-tUA9qTp0lMDL6oYRh31zC612W3CMLDESmKybNAFZjiHcHly6GkM2dofkVaXW3DcMpURKM_5iutL7F9IWDpKO7Vo7Ao9NxGhkf0i5Tbxq9CWgJjaYq7liXGuBYXfxPAAAAAYHumsQA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
STATS_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/e6c477b9b468885c9908e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
