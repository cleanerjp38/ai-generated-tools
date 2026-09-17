# 002-steam-randomizer

Steamからランダムにゲームを1本選び、タイトル・App ID・ストアURLを表示するCLIツール。

## 機能

実行するとSteamのゲーム検索結果からランダムに1ページを取得し、そのページに含まれるゲームから1本をランダムに選ぶ。

出力例：

```text
Today's random Steam game!
Game: Vampire Hunters
App ID: 2206270
https://store.steampowered.com/app/2206270/
```

## 使用技術

- Python 3
- Beautiful Soup 4
- urllib.request
- random

## 仕組み

```text
Steam検索ページ
    ↓
urllib.request でHTMLを取得
    ↓
BeautifulSoup でHTMLを解析
    ↓
ゲーム一覧を抽出
    ↓
random.choice() で1本選択
    ↓
タイトル・App ID・Steam URLを表示
```

## セットアップ

必要なライブラリをインストールする。

```powershell
python -m pip install -r requirements.txt
```

## 実行

```powershell
python main.py
```

## 開発中に起きた問題

当初はSteam Web APIからアプリ一覧を取得する予定だった。

旧APIを試したところ404エラーが発生したため、現行APIへの変更を検討した。

しかし、現行APIの利用にはSteam Web APIキーが必要で、APIキー取得にはSteam Guardモバイル認証機器が必要だった。

今回は小さなツールを短時間で完成させることを優先し、Steamの公開検索ページからHTMLを取得して解析する方式へ変更した。

## 学んだこと

- 外部APIは仕様変更や廃止が起こる
- APIを使うには認証が必要な場合がある
- APIが使えなくても、別のデータ取得方法を検討できる
- Beautiful Soupを使うとHTMLから必要な要素を抽出できる
- `random.choice()` でリストからランダムに要素を選べる
- 最初の設計に固執せず、目的に合わせて実装方法を変更することも開発の一部

## 注意

このツールはSteam上の全ゲームから厳密に均等な確率で抽選するものではない。

Steam検索結果のランダムなページを選び、そのページ内からランダムに1本を選択している。

そのため、Steam検索の並び順やページ構成の影響を受ける。