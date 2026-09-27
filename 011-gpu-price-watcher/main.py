import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://kakaku.com/pc/videocard/itemlist.aspx?pdf_Spec103=502&pdf_so=p1"
DATA_FILE = Path("prices.json")

response = requests.get(URL, timeout=10)
response.encoding = "shift_jis"

soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text(" ", strip=True)

prices = re.findall(r"¥([\d,]+)", text)

# 最安値を整数に変換
current_price = int(prices[0].replace(",", ""))
print(f"今回の最安値: {current_price:,}円")

prices = re.findall(r"¥([\d,]+)", text)

if not prices:
    print("価格を取得できませんでした")
    exit()

current_price = int(prices[0].replace(",", ""))

# 前回データを読み込む
if DATA_FILE.exists():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    previous_price = data["price"]
    print(f"前回の最安値: {previous_price:,}円")

    difference = current_price - previous_price

    if difference < 0:
        print(f"↓ {abs(difference):,}円 値下がり！")
    elif difference > 0:
        print(f"↑ {difference:,}円 値上がり")
    else:
        print("→ 価格変動なし")
else:
    print("前回データはありません")

# 今回の価格を保存
data = {
    "gpu": "GeForce RTX 5070",
    "price": current_price
}

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("今回の価格を保存しました")