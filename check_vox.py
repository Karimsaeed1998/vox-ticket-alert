import os
import requests

MOVIE_URL = "https://egy.voxcinemas.com/showtimes?c=city-centre-almaza"

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT = os.environ["TELEGRAM_CHAT_ID"]

html = requests.get(MOVIE_URL, timeout=20).text.lower()

trigger = "spider-man: brand new day" in html

if trigger:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT,
            "text": "🎟️ Spider-Man: Brand New Day is now showing on VOX!\n\n" + MOVIE_URL
        }
    )
else:
    print("❌ No tickets yet")
