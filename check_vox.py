import os
import requests
from bs4 import BeautifulSoup

MOVIE_URL = "https://egy.voxcinemas.com/showtimes?c=city-centre-almaza"

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT = os.environ["TELEGRAM_CHAT_ID"]

STATE_FILE = "last_showtimes.txt"

html = requests.get(MOVIE_URL, timeout=20).text.lower()

# Look for Spider-Man availability + booking indicators
keywords = [
    "spider-man",
    "brand new day",
    "book now",
    "showtimes"
]

available = all(word in html for word in keywords)

if available:
    current_state = "tickets_available"
else:
    current_state = "not_available"

try:
    with open(STATE_FILE, "r") as f:
        old_state = f.read().strip()
except:
    old_state = ""

if current_state != old_state and current_state == "tickets_available":
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT,
            "text": "🎬 Spider-Man: Brand New Day showtimes may be available!\n\nCheck VOX:\n" + MOVIE_URL
        }
    )

with open(STATE_FILE, "w") as f:
    f.write(current_state)

print("Current status:", current_state)
