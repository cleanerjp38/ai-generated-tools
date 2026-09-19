# 003 YouTube Transcript

YouTubeのURLから動画タイトルと字幕（文字起こし）を取得するPython製CLIツールです。

## Features

- YouTube URLから動画IDを取得
- 動画タイトルを取得
- 日本語字幕を優先して取得
- 日本語字幕がない場合は英語字幕を取得
- 字幕が無効な動画ではエラーメッセージを表示

## Requirements

- Python 3
- youtube-transcript-api
- yt-dlp

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage
```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

実行すると、動画タイトルと取得できた字幕がターミナルに表示されます。

## Notes

動画によっては字幕が無効になっていたり、利用可能な字幕が存在しない場合があります。

YouTubeの自動生成字幕を利用する場合、文字起こしには誤変換が含まれることがあります。

yt-dlpからJavaScript runtimeに関する警告が表示される場合がありますが、タイトル取得が正常に行える場合は本ツールの基本機能を利用できます。

## Tech
Python
youtube-transcript-api
yt-dlp