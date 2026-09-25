# 009 AI Generated Tools Launcher

AI Generated Toolsプロジェクトで作成したツールを、1つの画面から起動するためのランチャーです。

新しいツールを作るたびに `tools.json` に情報を追加することで、ランチャーのボタンも増えていきます。

## 機能

現在、001〜008のツールに対応しています。

- 001 YouTube Randomizer
- 002 Steam Randomizer
- 003 YouTube Transcript
- 004 Dice Roller
- 005 Random Browser Lock
- 006 NISA Simulator
- 007 News Randomizer
- 008 Comfort Dog

ツールの種類によって起動方法を切り替えます。

- Pythonツール → 新しいコンソールで実行
- HTMLツール → ブラウザで開く
- 引数が必要なPythonツール → 入力ダイアログを表示してから実行
- ブラウザ拡張 → 関連するWebページを開く

## 使用技術

- Python
- Tkinter
- JSON
- subprocess
- pathlib
- webbrowser

追加ライブラリは使用していません。

## ファイル構成

```text
009-ai-generated-tools-launcher/
├── main.py
├── tools.json
└── README.md
```

### main.py

ランチャー本体です。

`tools.json` を読み込み、登録されているツールの数だけボタンを自動生成します。

ボタンを押すと、ツールの種類に応じてPython、HTML、ブラウザ拡張などを起動します。

### tools.json

ランチャーに表示するツールの情報を管理します。

例：

```json
{
  "id": "006",
  "name": "NISA Simulator",
  "type": "html",
  "path": "../006-nisa-simulator/index.html"
}
```

新しいツールを追加するときは、基本的にこのファイルへ情報を追加します。

引数が必要なツールでは、次のように `argument` を指定できます。

```json
{
  "id": "003",
  "name": "YouTube Transcript",
  "type": "python",
  "path": "../003-youtube-transcript/main.py",
  "argument": "YouTube URL"
}
```

## 実行方法

このディレクトリで以下を実行します。

```powershell
python main.py
```

ランチャー画面が表示されるので、起動したいツールのボタンをクリックします。

## 仕組み

大まかな流れは次のとおりです。

```text
tools.json
    ↓
main.py が読み込む
    ↓
ツールごとのボタンを自動生成
    ↓
ボタンをクリック
    ↓
typeを確認
    ├── python    → 新しいコンソールで実行
    ├── html      → ブラウザで開く
    └── extension → 関連Webページを開く
```

ツールの一覧データと、ツールを起動する処理を分離しています。

そのため、新しいツールを追加するたびに `main.py` にボタンを追加する必要はありません。

## 今回学んだこと

- Tkinterを使った簡単なGUIの作成
- JSONファイルから設定を読み込む方法
- データからGUIのボタンを自動生成する方法
- `subprocess` を使って別のPythonプログラムを起動する方法
- 対話型CLIは専用のコンソールで起動すると扱いやすいこと
- `webbrowser` を使ってHTMLやWebページを開く方法
- 同じ「ツール」でも、Python、HTML、ブラウザ拡張では起動方法が異なること
- 設定データとプログラム本体を分離すると拡張しやすくなること

## 今後

AI Generated Toolsプロジェクトで新しいツールを作成するたびに、`tools.json` に追加していきます。

30個のツールが完成したとき、それらをまとめて起動できるランチャーへ成長させる予定です。