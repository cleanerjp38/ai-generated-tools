# 001 YouTube Randomizer

YouTubeのホーム画面に表示されているおすすめ動画から、
ランダムに1本のURLを選ぶChrome拡張機能。

## 目的

YouTubeのおすすめアルゴリズムによるパーソナライズは利用しつつ、
ランキングやサムネイルを自分で選ばず、偶然の動画に出会うためのツール。

## 使い方

1. ChromeでYouTubeのホーム画面を開く
2. YouTube Randomizerを開く
3. 「ランダムに1本選ぶ」を押す
4. 表示されたURLを開く

## 構成

- `manifest.json` - Chrome拡張機能の設定
- `popup.html` - 拡張機能の画面
- `popup.js` - 動画URLの取得とランダム選択

## 技術

- HTML
- JavaScript
- Chrome Extensions Manifest V3

## セキュリティ

APIキーやYouTubeの認証情報は使用しない。
現在開いているYouTubeページから動画URLのみを取得する。