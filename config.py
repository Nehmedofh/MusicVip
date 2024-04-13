import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "11480225"))
API_HASH = getenv("API_HASH", "4e246bace68111a0d82fa2ce96e0e5e3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7187507488:AAFLNq9CT1aPNNWgaTJz2jE2r64HZHY6eSY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://fridabisov26:feridabusov2@cluster0.rrmqdo9.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002096523173"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6671958102"))

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

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SohbettGrupus")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Botumsan")

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
STRING1 = getenv("STRING_SESSION", "AgCvLKEAiqdBIrT3EbvPyJnCTshQ9m8hj1iSlk4ONtOD_HwKsieA8e8RTjhFG_Sazvs0NBnHMLo7xarmbPBeLSnrHYMnVESNJwDTtnssCL-3hBJQQWkcKoPvk74_FSxmMvUmzwB7zID0g6eExWkQp2NukE23Eo8IUdLk45h7oC5f533AA5QNF7ebKmg7QqYjNp_BlKeJQYUoFka1tZY9WjtWePzmcQQydX18pox2sHpHPf1POrtQP7Gy4ZQFQCdEvgF5sMpRcYxkbnDWCnhp4BHqUC-80bclqrjErLepReyFSB46o08fFkuFrZxS7IiBdnFf_unHj1SOYjlQN562zPde7RZtzgAAAAGWVHwiAA")
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
    "START_IMG_URL", "https://telegra.ph/file/c53ec2eac685008587353.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/c53ec2eac685008587353.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
STATS_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/c53ec2eac685008587353.jpg"


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
