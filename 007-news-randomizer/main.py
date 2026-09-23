import random
from datetime import datetime

import requests
from bs4 import BeautifulSoup

URL = "https://smart.asahi.com/v/list/newslist.php"
BASE_URL = "https://smart.asahi.com"

response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

today = datetime.now().strftime("%m/%d")
articles = []

for link in links:
    href = link.get("href")
    title = link.get_text(strip=True)

    if (
        href
        and href.startswith("/v/article/")
        and f"({today} " in title
    ):
        article_url = BASE_URL + href
        articles.append((title, article_url))

print(f"今日（{today}）の記事数: {len(articles)}")
print()

sample_size = min(10, len(articles))
selected_articles = random.sample(articles, sample_size)

print(f"ランダムニュース {sample_size}本")
print("=" * 50)

for i, (title, url) in enumerate(selected_articles, start=1):
    print(f"{i}. {title}")
    print(url)
    print()