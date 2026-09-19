import sys
import yt_dlp
from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
)

def get_video_id(url):
    parsed = urlparse(url)

    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        query = parse_qs(parsed.query)
        return query.get("v", [None])[0]

    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")

    return None

def get_video_title(url):
    options = {
        "quiet": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title", "タイトル不明")

if len(sys.argv) < 2:
    print("使い方: python main.py <YouTube URL>")
    sys.exit(1)

url = sys.argv[1]
video_id = get_video_id(url)
title = get_video_title(url)
print(f"タイトル: {title}")
print()
print("--- 文字起こし ---")
print()

if video_id is None:
    print("動画IDを取得できませんでした。")
    sys.exit(1)

api = YouTubeTranscriptApi()

try:
    transcript = api.fetch(video_id, languages=["ja", "en"])

    for item in transcript:
        print(item.text)

except TranscriptsDisabled:
    print("この動画では字幕が無効になっています。")

except NoTranscriptFound:
    print("利用できる字幕が見つかりませんでした。")