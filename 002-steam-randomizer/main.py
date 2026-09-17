import random
import urllib.request
from bs4 import BeautifulSoup


# Steam検索結果の中からランダムなページを選ぶ
page = random.randint(1, 100)

url = (
    "https://store.steampowered.com/search/"
    f"?category1=998&page={page}"
)

# ブラウザからのアクセスに近い形でリクエストする
request = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(request) as response:
    html = response.read()

# HTMLを解析する
soup = BeautifulSoup(html, "html.parser")

# 検索結果に表示されたゲームを取得する
games = soup.select("a.search_result_row")

if not games:
    print("ゲームを取得できませんでした。")
    exit()

# そのページからランダムに1本選ぶ
game = random.choice(games)

title_element = game.select_one("span.title")
title = title_element.get_text(strip=True)

app_id = game.get("data-ds-appid")
game_url = f"https://store.steampowered.com/app/{app_id}/"

print("Today's random Steam game!")
print(f"Game: {title}")
print(f"App ID: {app_id}")
print(game_url)