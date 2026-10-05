````markdown
# 016 Chat Cleaner

ChatGPTなどの会話ログJSONから、不要なデータを削除して整形するPython CLIツール。

## Purpose

会話ログを後続ツールで扱いやすくするため、不要なメッセージや空白を取り除く。

GPTログ操作シリーズの前処理として使用する。

## Requirements

- Python 3
- 外部ライブラリ不要

## Cleaning rules

現在は以下の処理を行う。

1. `role` が `user` または `assistant` 以外のメッセージを削除
2. `text` が文字列ではないメッセージを削除
3. `text` 前後の空白を削除
4. `text` が空、または空白だけのメッセージを削除

## Input format

```json
[
  {
    "role": "user",
    "text": "  今日は016を作る  "
  },
  {
    "role": "assistant",
    "text": ""
  },
  {
    "role": "system",
    "text": "これは不要"
  },
  {
    "role": "assistant",
    "text": "  Chat Cleanerを作りましょう！  "
  }
]
```

## Usage

```powershell
python main.py sample.json
```

## Output

```json
[
  {
    "role": "user",
    "text": "今日は016を作る"
  },
  {
    "role": "assistant",
    "text": "Chat Cleanerを作りましょう！"
  }
]
```

## Structure

```text
016-chat-cleaner/
├── main.py
├── README.md
└── sample.json
```

## How it works

```text
conversation.json
        ↓
JSON読み込み
        ↓
roleをチェック
        ↓
textをチェック
        ↓
前後の空白を削除
        ↓
不要データを除外
        ↓
きれいなJSONを出力
```

## Key point

不要なデータを見つけた場合は `continue` を使い、そのデータの残りの処理を飛ばして次のメッセージへ進む。

```python
if role not in VALID_ROLES:
    continue
```

これにより、条件を満たさないデータを簡潔に除外できる。

## Relationship with previous tools

```text
014 User Message Extractor
    → user発言を抽出

015 Assistant Message Extractor
    → assistant発言を抽出

016 Chat Cleaner
    → 会話ログそのものを掃除
```

3つとも同じ `role` + `text` のJSON形式を利用する。

## Future ideas

- 重複メッセージの削除
- 改行の正規化
- UI由来の不要文字列の削除
- 結果をJSONファイルとして直接保存
- 実際のChatGPTログ形式への対応
- Conversation Mergerとの連携

## Notes

このツールはローカルのJSONファイルだけを処理する。

APIキーや認証情報は不要。
```` 