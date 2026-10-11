
# 017 Conversation Merger

複数のChatGPT会話ログJSONを1つのJSONファイルに結合するPython CLIツール。

## Purpose

複数の会話ログを統合し、後続の分析・日記生成ツールで扱いやすくする。

AI生成ツール30個プロジェクトの17番目。GPTログ操作シリーズの13-Dに該当する。

## Requirements

- Python 3
- 外部ライブラリ不要

## Usage

```powershell
python main.py sample1.json sample2.json -o merged.json
```

入力ファイルは3個以上でも指定できる。

`-o` は出力ファイルを指定するオプション。

## Input format

各入力ファイルは、次のようなJSON配列とする。

```json
[
  {
    "role": "user",
    "text": "今日はRustを勉強した"
  },
  {
    "role": "assistant",
    "text": "いいね！"
  }
]
```

## Output

指定した入力ファイルを順番に結合し、`merged.json` に保存する。

```text
sample1.json (3件)
sample2.json (2件)
       ↓
Conversation Merger
       ↓
merged.json (5件)
```

## Specifications

- 入力順を維持する
- 重複メッセージを削除しない
- 日時順の並び替えは行わない
- 入力JSONが配列であることを検証する
- 配列の各要素がオブジェクトであることを検証する
- 出力先が入力ファイルと同じ場合はエラーにする
- `role` や `text` の内容までは検証しない

## Structure

```text
017-conversation-merger/
├── main.py
├── README.md
├── sample1.json
└── sample2.json
```

`merged.json` は実行時に生成される出力ファイル。

## How it works

1. argparseで入力ファイルと出力先を取得する
2. pathlibでファイルを開く
3. json.load()でJSONを読み込む
4. extend()でメッセージを結合する
5. json.dumps()でJSON文字列に変換する
6. write_text()で出力ファイルへ保存する

## Key point

```python
merged.extend(messages)
```

`extend()` は配列の各要素を追加する。

`append()` とは異なり、配列の入れ子を作らずに結合できる。

## Relationship with previous tools

- 014 User Message Extractor：ユーザー発言の抽出
- 015 Assistant Message Extractor：Assistant発言の抽出
- 016 Chat Cleaner：不要データの削除
- 017 Conversation Merger：複数ログの結合

共通JSON形式を利用している。

## Future ideas

- 018 Chronological Sorterとの連携
- 会話タイトルや日時などのメタデータ保持
- 複数ログの一括読み込み
- ChatGPT Conversation Exporterとの連携
- ChatGPT Daily Journalへの統合

## Notes

ローカルのJSONファイルのみを処理する。

APIキーや認証情報は不要。

実際の会話ログには個人情報が含まれる可能性があるため、GitHubへ公開しないこと。
