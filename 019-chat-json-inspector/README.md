# 019 Chat JSON Inspector

ChatGPTの会話JSONファイルを検査するシンプルなWebツール。

AI生成ツール30個プロジェクトの19個目。

## 機能

- JSONファイルの読み込み
- ユーザー発言数の集計
- GPT発言数の集計
- 全発言数の集計
- 合計文字数の集計
- 空欄の発言の検出
- JSON形式エラーの検出
- 発言ごとの不正なrole・textの検出

## 使用技術

- HTML
- CSS
- JavaScript

外部ライブラリ・外部APIは使用しない。

## ファイル構成

```text
019-chat-json-inspector/
├── index.html
└── README.md
```

## 使い方

1. `index.html` をブラウザで開く
2. JSONファイルを選択する
3. 検査結果を確認する

## 対応JSON形式

```json
[
  {
    "role": "user",
    "text": "こんにちは"
  },
  {
    "role": "assistant",
    "text": "こんにちは！"
  }
]
```

## 動作の仕組み

1. File APIでローカルファイルを読み込む
2. `JSON.parse()` でJSONを解析する
3. 配列の各要素を調べる
4. `role` と `text` の形式を検査する
5. 発言数・文字数・エラー数を集計する
6. 結果を画面に表示する

## 既知の制限

- 会話の取得漏れは検出できない
- UI由来の文字列混入は検出できない
- `role` は `user` と `assistant` のみ対応
- 文字数はUnicodeコードポイント単位で集計する
- JSONファイルの修正機能はない
- JSONの最上位が配列でない場合、検査失敗となる

## セキュリティ

- ファイルはブラウザ内で処理する
- 外部サーバーへの送信は行わない
- APIキーや認証情報は使用しない
- 実際の会話ログはGitHubに含めない

## 開発目的

018 ChatGPT Conversation Exporterで保存したJSONを
簡単に検査できるようにする。

## プロジェクト

AI生成ツール30個プロジェクト

019 / 030