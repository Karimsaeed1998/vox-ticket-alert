import os, requests
from bs4 import BeautifulSoup
MOVIE_URL="https://egy.voxcinemas.com/movies/spider-man-brand-new-day"
TOKEN=os.environ["TELEGRAM_BOT_TOKEN"]
CHAT=os.environ["TELEGRAM_CHAT_ID"]
html=requests.get(MOVIE_URL,timeout=20).text.lower()
trigger=("view showtimes" in html) or ("book now" in html)
state=".state"
old=""
try: old=open(state).read().strip()
except: pass
new="1" if trigger else "0"
if new=="1" and old!="1":
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  data={"chat_id":CHAT,"text":"🎟️ VOX tickets appear to be available: "+MOVIE_URL})
open(state,"w").write(new)
