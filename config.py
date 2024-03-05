import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27715768"))
API_HASH = getenv("API_HASH", "7276a0bc7e5eafbeea78669fa0f3fd6b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7179850198:AAGPiTeqztaB_WiLQxsXXj7kZ2cSn-qz5sk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001952936217"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6885548094"))

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

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XOXANclub")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/XoxanClub")

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
STRING1 = getenv("STRING_SESSION", "AgGm6LgAKyePjb7FFLaixdeMDuQzej8aQ_K5joM-OhIsRt6D2fZTpCSxXsUEE6ZO_lahfYLuL4ix_mqbwP2ktHpgqZAB_kVxjrsFTzwzuc98kwpTT7GfvvZ737eRtjaEMO4evRGQVvx-jb_zXarJkybuo-_VasbRm5M0COsDaNYt_AlyhHcbf7hRzIdyF8cqhVuv-ys4l4y7veyDUtOrVTACTHiUGGbkGoAxPyEPzIMsKQL_Dw0Ecz9P1FeENLJ-mxQsDMtFb2mxtNWF7sR0w5J1CgAPnjdTGVbgwHqr_86XyJ5q5LKZRQicXTJF5b6S6wjKUiLDZVWuljKFJPcshT33xl6k5gAAAAGmP54ZAA")
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
    "START_IMG_URL", "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
STATS_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/05303ed3e30bd4940f57f.jpg"


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
