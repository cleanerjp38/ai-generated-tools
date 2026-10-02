````markdown
# 014 User Message Extractor

ChatGPTなどの会話ログJSONから、ユーザーの発言だけを抽出するPython CLIツール。

## Purpose

会話ログから `role` が `user` のメッセージだけを取り出す。

将来的には、ChatGPTの会話ログ整理・日記生成ツール群の部品として利用する予定。

## Requirements

- Python 3
- 外部ライブラリ不要

## Input format

以下のようなJSON配列を入力する。

```json
[
  {
    "role": "user",
    "text": "今日は風邪気味だワン。"
  },
  {
    "role": "assistant",
    "text": "無理せず進めましょう。"
  },
  {
    "role": "user",
    "text": "AI生成ツールを作るワン。"
  }
]
```

## Usage

```powershell
python main.py sample.json
```

## Output

```text
今日は風邪気味だワン。

AI生成ツールを作るワン。
```

## Structure

```text
014-user-message-extractor/
├── main.py
├── README.md
└── sample.json
```

## How it works

1. JSONファイルを読み込む
2. 各メッセージの `role` を確認する
3. `role == "user"` のメッセージだけを取り出す
4. `text` の内容を表示する

## Future ideas

- 抽出結果をMarkdownファイルへ保存する
- ChatGPTの実際のエクスポート形式へ対応する
- ブラウザ版ChatGPTから会話を取得するツールと連携する
- Assistant Message Extractorなど他の会話処理ツールと統合する

## Notes

このツール自体はChatGPTへ接続せず、ローカルのJSONファイルだけを処理する。

APIキーや認証情報は不要。
````