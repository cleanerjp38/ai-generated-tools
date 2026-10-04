````markdown
# 015 Assistant Message Extractor

ChatGPTなどの会話ログJSONから、Assistantの発言だけを抽出するPython CLIツール。

## Purpose

会話ログから `role` が `assistant` のメッセージだけを取り出す。

`014-user-message-extractor` と対になるツールで、今後のChatGPTログ整理・分析・日記生成ツール群の部品として利用する予定。

## Requirements

- Python 3
- 外部ライブラリ不要

## Input format

以下のようなJSON配列を入力する。

```json
[
  {
    "role": "user",
    "text": "今日は何を作る？"
  },
  {
    "role": "assistant",
    "text": "Assistant Message Extractorを作りましょう。"
  },
  {
    "role": "user",
    "text": "難しい？"
  },
  {
    "role": "assistant",
    "text": "014を流用できるので簡単です。"
  }
]
```

## Usage

```powershell
python main.py sample.json
```

## Output

```text
Assistant Message Extractorを作りましょう。

014を流用できるので簡単です。
```

## Structure

```text
015-assistant-message-extractor/
├── main.py
├── README.md
└── sample.json
```

## How it works

1. JSONファイルを読み込む
2. 各メッセージの `role` を確認する
3. `role == "assistant"` のメッセージだけを取り出す
4. `text` の内容を表示する

## Relationship with 014

`014-user-message-extractor` では、

```python
if message.get("role") == "user":
```

としてユーザー発言を抽出した。

015では、

```python
if message.get("role") == "assistant":
```

とすることで、同じ構造を使ってAssistant発言だけを抽出している。

## Future ideas

- 抽出結果をMarkdownファイルへ保存する
- ChatGPTの実際のエクスポート形式へ対応する
- ブラウザ版ChatGPTから取得した会話ログと連携する
- User Message Extractorと統合して任意のroleを抽出できるようにする
- Chat CleanerやDaily Chat Digestなど後続ツールへ接続する

## Notes

このツール自体はChatGPTへ接続せず、ローカルのJSONファイルだけを処理する。

APIキーや認証情報は不要。
````