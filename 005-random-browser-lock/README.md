# 005 Random Browser Lock

指定したWebサイトへのアクセスを、ランダムな時間だけブロックするBrave / Chrome拡張機能です。

現在のバージョンでは、YouTubeを1〜60分のランダムな時間ロックします。
ロック時間や解除時刻は画面に表示しません。

## 目的

「あと何分で解除されるか分からない」状態を作ることで、
なんとなくWebサイトを開いてしまう習慣を減らせるか試すために作りました。

## 機能

- LOCKボタンでロック開始
- 1〜60分からランダムにロック時間を決定
- 解除時刻をブラウザ内に保存
- ロック中はYouTubeをブロック
- ロック時間・解除時刻はユーザーに表示しない
- 時間経過後は自動的にアクセス可能になる

## ファイル構成

```text
005-random-browser-lock/
├── manifest.json
├── popup.html
├── popup.js
├── blocker.js
└── README.md
```

- `manifest.json` - 拡張機能の設定
- `popup.html` - 拡張機能のポップアップ画面
- `popup.js` - ランダムな解除時刻を生成・保存
- `blocker.js` - YouTubeを開いたときにロック状態を確認

## 使用技術

- HTML
- JavaScript
- Chrome Extensions Manifest V3
- Chrome Storage API
- Content Scripts

BraveはChromiumベースのため、Chrome拡張機能として実装しています。

## 使い方

1. Braveで `brave://extensions/` を開く
2. デベロッパーモードを有効にする
3. 「パッケージ化されていない拡張機能を読み込む」を選択
4. `005-random-browser-lock` フォルダを指定
5. 拡張機能のポップアップから `LOCK` を押す
6. ロック中にYouTubeを開くとブロック画面が表示される

## 現在の制限

これは習慣改善の効果を試すためのMVPです。

- 現在の対象サイトはYouTubeのみ
- 拡張機能を無効化すれば回避可能
- 別のブラウザを使えば回避可能
- 強制的なアクセス制限を目的としたものではない

## 今後の候補

- 複数サイトへの対応
- ブロック対象サイトを選択できる設定画面
- 任意URLの登録
- PCアプリ版
- Android版

## 作成日

2026-09-21