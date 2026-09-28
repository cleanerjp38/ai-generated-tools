# AI生成ツール候補ネタ帳 v1

## 目的

AI生成ツールプロジェクトのアイデアを、30分〜数時間程度で完成できる小さなツールへ分解したネタ帳。

最優先目標は、

**「とにかくツールを完成させること」**

完成度・実用性・規模は問わない。

大きなアイデアを一気に完成させるのではなく、

**要件を考える → 設計する → 実装する → 動かす → テストする → 修正する**

という開発サイクルを大量に経験する。

このリストは固定ロードマップではない。

その日の気分・体力・興味に応じて好きなものを拾ってよい。

予定外のツールを思いついた場合は、そちらを作ってもよい。

---

# 基本ルール

- 小さなツールでも1個として数える
    
- 独立した技術実験もツール候補とする
    
- 既存ツールの大きめのv2・派生版も数えてよい
    
- 類似機能を無理に別ツール扱いする必要はない
    
- 作る直前に粒度を再調整してよい
    
- 小ツールを後から統合したものも別ツールとして扱ってよい
    
- 全候補を作る必要はない
    
- 「ネタ切れしないための鉱山」として使う
    

## 難易度目安

- ★：かなり小さい。30分〜1時間程度を狙える
    
- ★★：少し考える。1〜数時間程度
    
- ★★★：API・外部サービス・新技術などを含む挑戦枠
    

---

# 1. 3Dキャラクター生成

## 1-A. Character Parameter Generator

身長、髪型、髪色、体型、服装などをランダム生成する。

- 完成条件：ボタン1つでキャラクター設定が表示される
    
- 難易度：★
    
- 技術：HTML / JavaScript
    
- 将来用途：3Dキャラクター生成の入力値
    

## 1-B. Character Parameter Preset

「大人っぽい」「スポーティー」などのプリセットから設定を生成する。

- 完成条件：プリセットを選ぶとキャラクター設定が出る
    
- 難易度：★
    

## 1-C. Character JSON Exporter

キャラクター設定をJSONとして保存する。

- 完成条件：設定をJSONファイルとして出力できる
    
- 難易度：★
    

## 1-D. Character JSON Loader

保存したキャラクターJSONを読み込む。

- 完成条件：JSONから設定を復元できる
    
- 難易度：★
    

## 1-E. Body Ratio Calculator

身長や頭身から各部位のおおまかなサイズを計算する。

- 完成条件：数値入力から身体比率を表示
    
- 難易度：★
    

## 1-F. Polygon Person Viewer

Three.jsで簡単な3D人型を表示する。

- 完成条件：ブラウザ上に立体人型が表示される
    
- 難易度：★★
    
- 新技術：Three.js
    

## 1-G. Random Polygon Person

3D人型の身長や比率をランダム化する。

- 完成条件：生成するたび違う人型になる
    
- 難易度：★★
    

## 1-H. Camera Rotate Viewer

3Dモデルをマウス操作で回転して見る。

- 完成条件：ドラッグ等で視点変更できる
    
- 難易度：★★
    
- 新技術：OrbitControls
    

## 1-I. Blender Primitive Human

Blender Pythonで球や円柱から簡単な人型を生成する。

- 完成条件：スクリプト実行で人型が生成される
    
- 難易度：★★
    
- 新技術：Blender Python API
    

## 1-J. Blender Random Human

Blender人型のサイズや比率をランダム化する。

- 完成条件：毎回少し違うモデルが生成される
    
- 難易度：★★
    

## 1-K. OBJ Export Experiment

生成したモデルをOBJ等で書き出す。

- 完成条件：3Dモデルファイルを保存できる
    
- 難易度：★★
    

## 1-L. Character Thumbnail Generator

キャラクター設定をプロフィールカード形式で表示する。

- 完成条件：名前・パラメータ・画像等が1画面に表示される
    
- 難易度：★〜★★
    

---

# 2. 水分摂取・Fitbit

## 2-A. Water Counter

水を飲んだ回数を記録する。

- 完成条件：「+1杯」で今日の杯数が増える
    
- 難易度：★
    

## 2-B. Water Counter with Reset

日付が変わったら杯数をリセットする。

- 完成条件：日単位で記録できる
    
- 難易度：★
    

## 2-C. Water Counter LocalStorage

杯数をブラウザに保存する。

- 完成条件：再起動後も記録が残る
    
- 難易度：★
    

## 2-D. Water Volume Calculator

杯数をmlへ換算する。

- 完成条件：1杯の量を設定して総水分量を表示
    
- 難易度：★
    

## 2-E. Water Goal Meter

1日の水分目標に対する進捗を表示する。

- 完成条件：進捗バー等で表示
    
- 難易度：★
    

## 2-F. Water Log

水を飲んだ時刻を記録する。

- 完成条件：操作ごとに時刻が履歴へ追加される
    
- 難易度：★
    

## 2-G. Water CSV Export

飲水履歴をCSVへ出力する。

- 完成条件：日付・時刻・量を保存できる
    
- 難易度：★
    

## 2-H. Water Weekly Graph

週間の水分摂取量をグラフ表示する。

- 完成条件：7日分を可視化
    
- 難易度：★★
    
- 新技術：Chart.js等
    

## 2-I. Water Reminder

一定時間水を飲んでいない場合に通知する。

- 完成条件：通知が表示される
    
- 難易度：★★
    

## 2-J. Fitbit API Login Test

Fitbit APIへの認証を試す。

- 完成条件：OAuth認証成功
    
- 難易度：★★★
    
- 新技術：OAuth
    

## 2-K. Fitbit Steps Reader

Fitbit APIから歩数を取得する。

- 完成条件：今日の歩数を表示
    
- 難易度：★★★
    

## 2-L. Fitbit Water Reader

Fitbitの水分記録を取得する。

- 完成条件：水分データを表示
    
- 難易度：★★★
    

## 2-M. Sensor Data Logger

スマホやウェアラブルの加速度データを保存する。

- 完成条件：センサデータを取得・保存
    
- 難易度：★★★
    

## 2-N. Drink Motion Detector Prototype

腕の動きから飲水らしい動きを簡易判定する。

- 完成条件：飲水候補動作を検出
    
- 難易度：★★★
    

## 2-O. Drink Detection Visualizer

センサ波形をグラフ化する。

- 完成条件：加速度等を可視化
    
- 難易度：★★
    

---

# 3. AI Generated Tools Launcher改造

## 3-A. Launcher Search

ツール名を検索する。

- 完成条件：文字入力でツールを絞り込める
    
- 難易度：★
    

## 3-B. Launcher Favorites

お気に入り機能を追加する。

- 完成条件：お気に入り登録・絞り込み
    
- 難易度：★
    

## 3-C. Launcher Categories

ツールを言語や種類で分類する。

- 完成条件：カテゴリ別表示
    
- 難易度：★
    

## 3-D. Launcher Tags

複数タグで分類する。

- 完成条件：タグ検索可能
    
- 難易度：★
    

## 3-E. Launcher Random

ツールをランダムに1個選ぶ。

- 完成条件：「今日作る/使うツール」をランダム表示
    
- 難易度：★
    

## 3-F. Launcher Recent

最近使ったツールを表示する。

- 完成条件：起動履歴を保存
    
- 難易度：★
    

## 3-G. Launcher Usage Count

各ツールの起動回数を記録する。

- 完成条件：利用回数ランキングを表示
    
- 難易度：★
    

## 3-H. Launcher Stats

ツール数や言語別個数を集計する。

- 完成条件：統計画面を表示
    
- 難易度：★
    

## 3-I. Launcher Status

Done / WIP / Archived等の状態を管理する。

- 完成条件：状態別に表示
    
- 難易度：★
    

## 3-J. Launcher Screenshot

各ツールにスクリーンショットを表示する。

- 完成条件：一覧や詳細画面に画像表示
    
- 難易度：★
    

## 3-K. Launcher Description

各ツールの説明を表示する。

- 完成条件：詳細ビューを追加
    
- 難易度：★
    

## 3-L. Launcher Auto Scan

ツールフォルダを自動走査する。

- 完成条件：フォルダ追加だけでツール一覧へ反映
    
- 難易度：★★
    

## 3-M. Launcher README Parser

READMEから名前や説明を取得する。

- 完成条件：README情報を自動取得
    
- 難易度：★★
    

## 3-N. Launcher Keyboard Navigation

キーボード操作に対応する。

- 完成条件：矢印キーとEnter等で操作
    
- 難易度：★
    

## 3-O. Launcher Dark Mode

ダークモードを追加する。

- 完成条件：テーマ切替・保存
    
- 難易度：★
    

## 3-P. Launcher v2 UI

UI全体を再設計する。

- 完成条件：旧版と明確に異なるUI
    
- 難易度：★★
    

## 3-Q. Launcher Export

ツール一覧をMarkdown等に出力する。

- 完成条件：TOOLS.md等を生成
    
- 難易度：★
    

## 3-R. Launcher Backlog

未完成のツール候補も表示する。

- 完成条件：完成品とアイデアを同じ画面で管理
    
- 難易度：★
    

---

# 4. Comfort Dog派生

## 4-A. Random Message Dog

慰めメッセージをランダム表示する。

- 完成条件：ボタンで文言切替
    
- 難易度：★
    

## 4-B. Mood Dog

気分別に慰める。

- 完成条件：「不安」「疲れた」等を選択
    
- 難易度：★
    

## 4-C. Work Dog

仕事疲れ専用版。

- 完成条件：仕事向けメッセージ表示
    
- 難易度：★
    

## 4-D. Study Dog

勉強・開発疲れ専用版。

- 完成条件：学習向けメッセージ表示
    
- 難易度：★
    

## 4-E. Morning Dog

朝向けメッセージ版。

- 難易度：★
    

## 4-F. Night Dog

夜・就寝前向け版。

- 難易度：★
    

## 4-G. Angry Dog

イライラしている時向け。

- 難易度：★
    

## 4-H. Tiny Dog

一言だけ表示する超短文版。

- 難易度：★
    

## 4-I. Long Dog

少し長めの文章で慰める。

- 難易度：★
    

## 4-J. Dog Message Editor

メッセージを自分で追加・削除する。

- 完成条件：GUIから文章編集
    
- 難易度：★
    

## 4-K. Dog JSON Messages

メッセージをJSONへ分離する。

- 完成条件：コードを書き換えず文言編集可能
    
- 難易度：★
    

## 4-L. Dog Favorite Message

好きな言葉を保存する。

- 難易度：★
    

## 4-M. Dog History

過去に表示された言葉を記録する。

- 難易度：★
    

## 4-N. Dog Daily Message

日替わりでメッセージを固定する。

- 難易度：★
    

## 4-O. Dog Notification

犬から通知を出す。

- 難易度：★★
    

## 4-P. Comfort Cat

猫版Comfort Dog。

- 難易度：★
    

## 4-Q. Comfort Old Man

別人格版。

- 難易度：★
    

## 4-R. Comfort Dog v2

気分選択、履歴、お気に入り等を統合する。

- 難易度：★★
    

---

# 5. Comfort Dog Android

## 5-A. Android Hello Dog

Android画面に犬と文字を表示する。

- 完成条件：実機またはエミュレータで起動
    
- 難易度：★★
    
- 新技術：Kotlin / Jetpack Compose
    

## 5-B. Android Dog Button

ボタンでメッセージを変更する。

- 難易度：★★
    

## 5-C. Random Message Android

ランダムメッセージを表示する。

- 難易度：★★
    

## 5-D. Mood Selector Android

気分選択を追加する。

- 難易度：★★
    

## 5-E. Dog Image Android

犬画像を表示する。

- 難易度：★★
    

## 5-F. Dark Mode Android

Androidのダークモード対応。

- 難易度：★★
    

## 5-G. Local Save Android

お気に入り等を端末保存する。

- 難易度：★★
    
- 新技術：DataStore
    

## 5-H. Dog Notification Android

Android通知を出す。

- 難易度：★★
    

## 5-I. Scheduled Dog Notification

決まった時刻に通知する。

- 難易度：★★★
    
- 新技術：WorkManager / AlarmManager
    

## 5-J. Dog Home Widget

ホーム画面ウィジェットを作る。

- 難易度：★★★
    

## 5-K. Share Dog Message

犬の言葉を他アプリへ共有する。

- 難易度：★★
    

## 5-L. Comfort Dog APK v1

基本機能を統合して実機利用する。

- 難易度：★★
    

## 5-M. Android Version Checker

アプリのバージョンを表示する。

- 難易度：★
    

## 5-N. Dog Settings Screen

通知やカテゴリの設定画面を作る。

- 難易度：★★
    

---

# 6. 人口シミュレーション

## 6-A. Birth Simulator

出生数だけ計算する。

- 完成条件：人口・出生率→出生数
    
- 難易度：★
    

## 6-B. Death Simulator

死亡数だけ計算する。

- 難易度：★
    

## 6-C. Migration Simulator

移民・人口流出入を計算する。

- 難易度：★
    

## 6-D. Population Growth Calculator

出生・死亡・移民を簡単な増減率として扱う。

- 難易度：★
    

## 6-E. Age Three Groups Simulator

0〜14歳、15〜64歳、65歳以上の3階級を扱う。

- 難易度：★★
    

## 6-F. Aging Rate Calculator

高齢化率を計算する。

- 難易度：★
    

## 6-G. Dependency Ratio Calculator

扶養人口比率を計算する。

- 難易度：★
    

## 6-H. Births Needed Calculator

人口維持に必要な出生数を逆算する。

- 難易度：★
    

## 6-I. Population Half-Life Calculator

一定人口減少率で何年後に半減するか計算する。

- 難易度：★
    

## 6-J. Population Scenario Comparator

複数の人口シナリオを比較する。

- 難易度：★★
    

## 6-K. Population Chart Viewer

CSVから人口グラフを表示する。

- 難易度：★★
    

## 6-L. Population Pyramid Viewer

人口ピラミッドを描画する。

- 難易度：★★
    

## 6-M. Prefecture Population Comparator

都道府県人口を比較する。

- 難易度：★★
    

## 6-N. Japan Population Simulator v2

出生・死亡・移民を分離した010改良版。

- 難易度：★★
    

## 6-O. Japan Population Simulator v3

年齢3階級を導入した改良版。

- 難易度：★★★
    

## 6-P. Parameter Sensitivity Tester

パラメータ変更の影響を比較する。

- 難易度：★★
    

---

# 7. YouTube × ChatGPT

## 7-A. YouTube URL Copier

YouTube URLをワンクリックコピー。

- 難易度：★
    

## 7-B. Transcript Copier

字幕取得後にクリップボードへコピー。

- 難易度：★〜★★
    

## 7-C. Transcript Cleaner

字幕の余計な改行や情報を削除する。

- 難易度：★
    

## 7-D. Transcript Character Counter

字幕の文字数等を計測する。

- 難易度：★
    

## 7-E. Transcript Chunker

長い字幕を指定文字数ごとに分割する。

- 難易度：★
    

## 7-F. YouTube Summary Prompt Generator

字幕から要約用プロンプトを生成する。

- 難易度：★
    

## 7-G. YouTube Q&A Prompt Generator

動画内容への質問用プロンプトを作る。

- 難易度：★
    

## 7-H. YouTube Study Prompt Generator

学習問題生成用プロンプトを作る。

- 難易度：★
    

## 7-I. Random Video Transcript Pipeline

001と003をつなぐ。

- 完成条件：ランダム動画→字幕取得
    
- 難易度：★★
    

## 7-J. Random Video Summary Package

ランダム動画→字幕→要約プロンプト。

- 難易度：★★
    

## 7-K. Clipboard Prompt Launcher

生成したプロンプトをコピーする。

- 難易度：★
    

## 7-L. ChatGPT Web Opener

プロンプトコピー後にChatGPTを開く。

- 難易度：★
    

## 7-M. Windows ChatGPT Launcher

ChatGPT Windows版を起動する。

- 難易度：★★
    

## 7-N. Send-to-ChatGPT Experiment

クリップボード等からChatGPTへ渡す方法を試す。

- 難易度：★★〜★★★
    

## 7-O. YouTube Assistant v1

URL→字幕→整形→プロンプト生成を統合。

- 難易度：★★
    

---

# 8. Obsidian保存ツール

## 8-A. Markdown Quick Memo

入力した文章をMarkdown保存する。

- 難易度：★
    

## 8-B. Timestamp Memo

日時つきでMarkdown保存する。

- 難易度：★
    

## 8-C. Daily Note Creator

今日の日付のMarkdownファイルを作る。

- 難易度：★
    

## 8-D. Daily Note Appender

今日の日次ノートへ追記する。

- 難易度：★
    

## 8-E. Clipboard to Markdown

クリップボード内容をMarkdown保存する。

- 難易度：★
    

## 8-F. Obsidian Inbox

Inbox.mdへ何でも追記する。

- 難易度：★
    

## 8-G. Tag Inserter

保存時にタグを追加する。

- 難易度：★
    

## 8-H. Frontmatter Generator

YAML frontmatterを生成する。

- 難易度：★
    

## 8-I. Template Memo

用途別テンプレートからノートを作る。

- 難易度：★
    

## 8-J. One-Button Diary

短文を今日の日記へ即保存する。

- 難易度：★
    

## 8-K. Screenshot Note Saver

スクリーンショットと文章をノートへ保存する。

- 難易度：★★
    

## 8-L. Voice Memo to Obsidian

音声→文字→Markdown保存。

- 難易度：★★★
    

## 8-M. Obsidian Search CLI

Vault内Markdownを検索する。

- 難易度：★〜★★
    

## 8-N. Obsidian Recent Notes

最近更新したノートを表示する。

- 難易度：★
    

## 8-O. Obsidian Quick Capture v1

入力・タグ・テンプレート・追記を統合する。

- 難易度：★★
    

---

# 9. 2D RPG

## 9-A. ASCII Player Movement

文字キャラクターを上下左右に動かす。

- 難易度：★
    

## 9-B. Tile Player Movement

画像キャラクターをマップ上で移動させる。

- 難易度：★★
    

## 9-C. Wall Collision Demo

壁を通れないようにする。

- 難易度：★〜★★
    

## 9-D. Map Loader

CSVやJSONからマップを読み込む。

- 難易度：★★
    

## 9-E. Map Editor

簡単なマップエディタ。

- 難易度：★★
    

## 9-F. NPC Random Walker

NPCをランダム移動させる。

- 難易度：★〜★★
    

## 9-G. NPC Talk Demo

NPCとの会話を実装する。

- 難易度：★〜★★
    

## 9-H. Dialogue Choice Demo

選択肢つき会話を実装する。

- 難易度：★★
    

## 9-I. Random Encounter Demo

歩いているとランダムエンカウントする。

- 難易度：★
    

## 9-J. Simple Battle

HPと攻撃だけの戦闘。

- 難易度：★
    

## 9-K. Turn Battle

敵と交互に攻撃するターン制戦闘。

- 難易度：★★
    

## 9-L. Damage Calculator

攻撃力・防御力からダメージ計算。

- 難易度：★
    

## 9-M. Experience Calculator

経験値からレベルを計算する。

- 難易度：★
    

## 9-N. Level Up Demo

経験値によって能力値を上げる。

- 難易度：★〜★★
    

## 9-O. Inventory

アイテム一覧と使用機能。

- 難易度：★★
    

## 9-P. Item Pickup

マップ上のアイテムを拾う。

- 難易度：★★
    

## 9-Q. Equipment Demo

武器などを装備する。

- 難易度：★★
    

## 9-R. Shop

アイテムの購入・売却。

- 難易度：★★
    

## 9-S. Quest Demo

NPCから依頼を受けて達成する。

- 難易度：★★
    

## 9-T. Save Data

ゲーム状態を保存・復元する。

- 難易度：★★
    

## 9-U. Random Dungeon

ランダム迷路・ダンジョンを生成する。

- 難易度：★★〜★★★
    

## 9-V. Treasure Chest Demo

宝箱からランダムアイテムを取得する。

- 難易度：★
    

## 9-W. Status Screen

HP、Lv、所持金などを表示する。

- 難易度：★
    

## 9-X. Tiny RPG v1

移動・会話・戦闘を統合した短編ゲーム。

- 難易度：★★★
    

---

# 10. 数値・選択肢RPG＋GPT

## 10-A. Choice Adventure

選択肢だけで進む短編ゲーム。

- 難易度：★
    

## 10-B. HP Choice RPG

選択肢でHPが増減する。

- 難易度：★
    

## 10-C. Money Choice RPG

所持金だけを管理するRPG。

- 難易度：★
    

## 10-D. Multi Stat RPG

HP・金・好感度等を管理する。

- 難易度：★〜★★
    

## 10-E. Random Event RPG

ランダムイベントを表示する。

- 難易度：★
    

## 10-F. Weighted Event RPG

イベントごとの発生確率を変える。

- 難易度：★
    

## 10-G. Event JSON Loader

イベントをJSONから読み込む。

- 難易度：★〜★★
    

## 10-H. Event JSON Editor

イベントJSONをGUIで作る。

- 難易度：★★
    

## 10-I. Branching Story Viewer

JSONの分岐ストーリーを実行する。

- 難易度：★★
    

## 10-J. Ending Checker

ステータス条件でエンディングを変える。

- 難易度：★
    

## 10-K. Random Character RPG

主人公能力をランダム生成。

- 難易度：★
    

## 10-L. Random Enemy Generator

敵の名前や能力を生成する。

- 難易度：★
    

## 10-M. Event Prompt Generator

GPT用イベント生成プロンプトを作る。

- 難易度：★
    

## 10-N. GPT Event JSON Validator

AI生成JSONを検証する。

- 難易度：★〜★★
    

## 10-O. GPT Event Importer

GPT生成イベントをゲームへ読み込む。

- 難易度：★★
    

## 10-P. Event History Viewer

過去イベント・選択を表示する。

- 難易度：★
    

## 10-Q. Save/Load Choice RPG

ゲーム途中の状態を保存する。

- 難易度：★〜★★
    

## 10-R. Procedural Event RPG

テンプレートからイベントを自動生成する。

- 難易度：★★
    

## 10-S. AI Event RPG v1

LLM APIからイベントを1つ生成する。

- 難易度：★★★
    

## 10-T. Endless Text RPG

AIイベントを繰り返し生成する。

- 難易度：★★★
    

---

# 11. ChatGPT使用時間計測

## 11-A. ChatGPT Page Timer

ChatGPTを開いている時間を計測する。

- 難易度：★〜★★
    

## 11-B. Active Tab Timer

ChatGPTがアクティブな時だけ計測する。

- 難易度：★★
    
- 新技術：Chrome Tabs API
    

## 11-C. Idle Aware Timer

離席時間を除外する。

- 難易度：★★
    

## 11-D. Daily Usage Recorder

日ごとの利用時間を保存する。

- 難易度：★〜★★
    

## 11-E. Weekly Usage Viewer

週間利用時間を表示する。

- 難易度：★〜★★
    

## 11-F. Usage Bar Chart

利用時間をグラフ化する。

- 難易度：★★
    

## 11-G. Session Timer

利用セッションごとに時間を記録する。

- 難易度：★★
    

## 11-H. Long Session Alert

一定時間連続利用すると通知する。

- 難易度：★★
    

## 11-I. Website Time Tracker

任意サイトの利用時間を記録する。

- 難易度：★★
    

## 11-J. ChatGPT Usage CSV Exporter

利用履歴をCSVへ出力する。

- 難易度：★
    

## 11-K. ChatGPT Usage Dashboard

今日・週・月の利用状況をまとめる。

- 難易度：★★
    

---

# 12. ChatGPT発言時刻記録

## 12-A. Manual Timestamp Logger

ボタンを押した時刻を保存する。

- 難易度：★
    

## 12-B. Text + Timestamp Logger

文章と時刻をセットで保存する。

- 難易度：★
    

## 12-C. Clipboard Timestamp Logger

コピーした文章と時刻を記録する。

- 難易度：★
    

## 12-D. ChatGPT DOM Message Finder

ChatGPTページ内の自分の発言を見つける。

- 難易度：★★
    

## 12-E. ChatGPT Message Extractor

ユーザー発言を一覧化する。

- 難易度：★★
    

## 12-F. Message Timestamp Injector

画面上の発言に時刻を追加表示する。

- 難易度：★★〜★★★
    

## 12-G. Chat Message Logger

新規発言を検知して保存する。

- 難易度：★★★
    

## 12-H. Conversation Start/End Logger

会話開始・終了時刻を記録する。

- 難易度：★★
    

## 12-I. Chat Timeline Exporter

発言を時系列Markdownへ出力する。

- 難易度：★★
    

## 12-J. Daily Message Count

1日の発言数を数える。

- 難易度：★★
    

## 12-K. Chat Activity Heatmap

時間帯ごとの発言量を可視化する。

- 難易度：★★
    

## 12-L. ChatGPT Logger v1

本文・時刻・会話情報等をまとめて保存する。

- 難易度：★★★
    

---

# 13. ChatGPTログから日記生成

## 13-A. User Message Extractor

自分の発言だけ抽出する。

- 難易度：★〜★★
    

## 13-B. Assistant Message Extractor

GPT発言だけ抽出する。

- 難易度：★
    

## 13-C. Chat Cleaner

ログ内の不要情報を削除する。

- 難易度：★
    

## 13-D. Conversation Merger

複数会話ログをまとめる。

- 難易度：★
    

## 13-E. Chronological Sorter

ログを時刻順に並べる。

- 難易度：★
    

## 13-F. Topic Keyword Counter

頻出単語を集計する。

- 難易度：★
    

## 13-G. Topic Splitter

ログを話題別に分類する。

- 難易度：★★
    

## 13-H. Chat Summary Prompt Generator

日次要約用プロンプトを生成する。

- 難易度：★
    

## 13-I. Diary Prompt Generator

日記生成用プロンプトを作る。

- 難易度：★
    

## 13-J. Development Diary Generator

開発関連ログだけ抽出する。

- 難易度：★★
    

## 13-K. Learning Diary Generator

学習関連ログだけ抽出する。

- 難易度：★★
    

## 13-L. Mood Word Counter

感情関連語の出現数を数える。

- 難易度：★
    

## 13-M. Chat Diary Markdown Exporter

整理したログをMarkdown保存する。

- 難易度：★
    

## 13-N. Daily Chat Digest

1日の話題・発言数・代表発言等をまとめる。

- 難易度：★★
    

## 13-O. AI Diary Generator

LLM APIでログを日記に変換する。

- 難易度：★★★
    

## 13-P. ChatGPT Daily Journal v1

ログ取得からMarkdown日記生成まで統合する。

- 難易度：★★★
    

---

# 14. Zennスクラップ分析

## 14-A. Zenn Scrap URL Collector

スクラップURLを一覧管理する。

- 難易度：★
    

## 14-B. Zenn Scrap Downloader

スクラップ本文を取得する。

- 難易度：★★
    

## 14-C. Zenn Scrap Title Extractor

タイトルを取得する。

- 難易度：★〜★★
    

## 14-D. Zenn Comment Counter

投稿数を数える。

- 難易度：★★
    

## 14-E. Zenn Date Extractor

投稿日時を取得する。

- 難易度：★★
    

## 14-F. Zenn Markdown Converter

取得内容をMarkdownへ変換する。

- 難易度：★★
    

## 14-G. Zenn Keyword Search

投稿内キーワード検索。

- 難易度：★
    

## 14-H. Zenn Keyword Counter

キーワードの出現数を数える。

- 難易度：★
    

## 14-I. Zenn Study Timeline

学習内容を時系列表示する。

- 難易度：★★
    

## 14-J. Zenn Learning Days Counter

投稿した学習日数を数える。

- 難易度：★
    

## 14-K. Zenn Monthly Activity

月ごとの投稿量を集計する。

- 難易度：★
    

## 14-L. Zenn Progress Chart

投稿量をグラフ化する。

- 難易度：★★
    

## 14-M. Zenn Topic Classifier

内容をRust、AtCoder等へ分類する。

- 難易度：★★
    

## 14-N. Zenn Summary Prompt Generator

スクラップ要約用プロンプトを作る。

- 難易度：★
    

## 14-O. Zenn Growth Report

期間ごとの学習内容の変化を整理する。

- 難易度：★★
    

## 14-P. Zenn Backup Tool

スクラップ全文を保存する。

- 難易度：★★
    

## 14-Q. Zenn Learning Analyzer v1

取得・集計・可視化・要約素材生成を統合する。

- 難易度：★★★
    

---

# 15. 画像検索・Google Lens的ツール

## 15-A. Clipboard Image Saver

クリップボード画像をPNG保存する。

- 難易度：★〜★★
    

## 15-B. Screenshot Saver

画面全体を保存する。

- 難易度：★
    

## 15-C. Region Screenshot Tool

画面の一部分を切り抜いて保存する。

- 難易度：★★
    

## 15-D. Image Crop Tool

画像を手動トリミングする。

- 難易度：★★
    

## 15-E. Image Resize Tool

画像サイズを変更する。

- 難易度：★
    

## 15-F. Image Format Converter

PNG、JPEG、WebP等を変換する。

- 難易度：★
    

## 15-G. Reverse Image Search Launcher

画像検索サービスを素早く開く。

- 難易度：★〜★★
    

## 15-H. Browser Context Menu Image Search

右クリックから画像検索する。

- 難易度：★★
    
- 新技術：Chrome ContextMenus API
    

## 15-I. Image URL Copier

画像URLをコピーする。

- 難易度：★
    

## 15-J. OCR Image Reader

画像から文字を読み取る。

- 難易度：★★〜★★★
    

## 15-K. OCR Clipboard Tool

コピー画像→OCR→テキストコピー。

- 難易度：★★★
    

## 15-L. Image Metadata Viewer

画像サイズ、形式、容量等を表示する。

- 難易度：★
    

## 15-M. Similar Image Search Prep Tool

画像を検索向けにリサイズ・変換する。

- 難易度：★
    

## 15-N. Screenshot → Search Pipeline

スクショ→保存→画像検索をまとめる。

- 難易度：★★
    

## 15-O. Brave Image Search Extension

Brave右クリックから画像検索する。

- 難易度：★★
    

## 15-P. Windows Snip Search Tool

デスクトップ画像を切り抜いて検索する。

- 難易度：★★〜★★★
    

## 15-Q. Lens-like Helper v1

スクショ、切り抜き、OCR、画像検索等を統合する。

- 難易度：★★★
    

---

# 16. おやつチケット

## 16-A. Snack Register

おやつ名とカロリーを登録する。

- 難易度：★
    

## 16-B. Snack Preset Button

よく食べるものをワンタップ登録する。

- 難易度：★
    

## 16-C. Snack Daily Total

今日のおやつkcal合計を表示する。

- 難易度：★
    

## 16-D. Snack Ticket Counter

今日のおやつ回数を表示する。

- 難易度：★
    

## 16-E. Snack History

日時つき履歴を表示する。

- 難易度：★
    

## 16-F. Snack LocalStorage

記録をブラウザ保存する。

- 難易度：★
    

## 16-G. Snack CSV Export

履歴をCSV出力する。

- 難易度：★
    

## 16-H. Snack Calendar

日別利用回数をカレンダー表示する。

- 難易度：★★
    

## 16-I. Snack Weekly Chart

週間の回数やkcalをグラフ化する。

- 難易度：★★
    

## 16-J. Snack Search

登録済みのおやつを検索する。

- 難易度：★
    

## 16-K. Snack Favorites

お気に入りおやつを登録する。

- 難易度：★
    

## 16-L. Snack Quick Add Widget

最小UIで即記録する。

- 難易度：★★
    

## 16-M. Snack Ticket Android

Androidからワンタップ記録する。

- 難易度：★★〜★★★
    

## 16-N. Snack Ticket v2

プリセット・履歴・合計等を統合する。

- 難易度：★★
    

---

# 17. AI掲示板

## 17-A. Fake Thread Viewer

2ちゃんねる風UIを表示する。

- 難易度：★
    

## 17-B. Anonymous Name Generator

匿名名を生成する。

- 難易度：★
    

## 17-C. Random ID Generator

掲示板風IDを生成する。

- 難易度：★
    

## 17-D. Timestamp Generator

レス投稿時刻を生成する。

- 難易度：★
    

## 17-E. Thread Post Form

自分でレスを書き込む。

- 難易度：★
    

## 17-F. Auto Reply Bot

定型文から自動返信する。

- 難易度：★
    

## 17-G. Personality Bot

人格ごとに返信内容を変える。

- 難易度：★★
    

## 17-H. Multi Bot Thread

複数人格同士を会話させる。

- 難易度：★★
    

## 17-I. Thread JSON Saver

スレッドをJSON保存する。

- 難易度：★
    

## 17-J. Thread JSON Loader

保存したスレを読み込む。

- 難易度：★
    

## 17-K. Thread Search

スレッド内検索。

- 難易度：★
    

## 17-L. Quote Reply

`>>12`形式のレス参照を実装する。

- 難易度：★★
    

## 17-M. Thread Generator Prompt

AIスレ生成用プロンプトを作る。

- 難易度：★
    

## 17-N. GPT Thread Importer

AI生成スレを読み込む。

- 難易度：★★
    

## 17-O. AI Thread v1

テーマからAPIでスレッドを生成する。

- 難易度：★★★
    

## 17-P. Infinite AI Board

AIレスによってスレッドを伸ばし続ける。

- 難易度：★★★
    

---

# 18. note記事分析

## 18-A. Note URL List

記事URLを管理する。

- 難易度：★
    

## 18-B. Note Article Downloader

note記事本文を取得する。

- 難易度：★★
    

## 18-C. Note Title Extractor

記事タイトルを取得する。

- 難易度：★〜★★
    

## 18-D. Note Date Extractor

投稿日を取得する。

- 難易度：★〜★★
    

## 18-E. Note Author Extractor

著者名を取得する。

- 難易度：★〜★★
    

## 18-F. Multi Note Downloader

複数記事を一括取得する。

- 難易度：★★
    

## 18-G. Note Markdown Converter

記事本文をMarkdown化する。

- 難易度：★★
    

## 18-H. Note Chronological Sorter

記事を投稿日順に並べる。

- 難易度：★
    

## 18-I. Note Keyword Search

記事群からキーワード検索する。

- 難易度：★
    

## 18-J. Note Keyword Trend

時期ごとのキーワード出現量を見る。

- 難易度：★★
    

## 18-K. Note Topic Classifier

記事を話題別に分類する。

- 難易度：★★
    

## 18-L. Note Timeline Builder

記事から時系列年表を作る。

- 難易度：★★
    

## 18-M. Change Detector

初期と最近の記事の語彙等を比較する。

- 難易度：★★
    

## 18-N. Note Summary Prompt Generator

複数記事要約用プロンプトを作る。

- 難易度：★
    

## 18-O. Life Timeline Prompt

人生・考え方の変化を整理するAIプロンプトを作る。

- 難易度：★
    

## 18-P. Note Archive Tool

記事群をローカルへ保存する。

- 難易度：★★
    

## 18-Q. Note Life Analyzer v1

記事取得、時系列化、要約素材生成を統合する。

- 難易度：★★★
    

---

# 19. 二人用交換日記

## 19-A. Single Diary

一人用日記アプリ。

- 難易度：★〜★★
    

## 19-B. Two User Diary

二人の投稿を区別する。

- 難易度：★★
    

## 19-C. Diary Timeline

投稿を時系列表示する。

- 難易度：★
    

## 19-D. Diary Edit

投稿編集機能。

- 難易度：★〜★★
    

## 19-E. Diary Delete

投稿削除機能。

- 難易度：★
    

## 19-F. Flower Reaction

投稿へ🌸等のリアクションをつける。

- 難易度：★〜★★
    

## 19-G. Read Status

既読・未読を管理する。

- 難易度：★★
    

## 19-H. Diary Password

簡単なログイン・認証を追加する。

- 難易度：★★〜★★★
    

## 19-I. Diary LocalStorage

日記データをブラウザ保存する。

- 難易度：★
    

## 19-J. Diary Firebase

日記をクラウド共有する。

- 難易度：★★★
    
- 新技術：Firebase
    

## 19-K. Image Attachment

日記へ画像を添付する。

- 難易度：★★〜★★★
    

## 19-L. Diary Search

過去の日記を検索する。

- 難易度：★
    

## 19-M. Diary Monthly Archive

月別に日記を表示する。

- 難易度：★
    

## 19-N. Diary Export

日記をMarkdownやJSONへ出力する。

- 難易度：★
    

## 19-O. Diary Notification

新規投稿を通知する。

- 難易度：★★★
    

## 19-P. Exchange Diary v1

投稿・既読・リアクション・共有保存等を統合する。

- 難易度：★★★
    

---

# 20. 二人用共有家計簿

## 20-A. Expense Input

支出を登録する。

- 難易度：★
    

## 20-B. Expense List

支出履歴を表示する。

- 難易度：★
    

## 20-C. Expense Edit

支出を編集する。

- 難易度：★
    

## 20-D. Expense Delete

支出を削除する。

- 難易度：★
    

## 20-E. Category Total

カテゴリ別合計を出す。

- 難易度：★
    

## 20-F. Monthly Total

月間支出を集計する。

- 難易度：★
    

## 20-G. Two Person Payer

どちらが払ったか記録する。

- 難易度：★
    

## 20-H. Split Calculator

二人の精算額を計算する。

- 難易度：★〜★★
    

## 20-I. Shared vs Personal Expense

共有費・個人費を分類する。

- 難易度：★
    

## 20-J. Expense Chart

支出をグラフ化する。

- 難易度：★★
    

## 20-K. Budget Limit

月予算と残額を表示する。

- 難易度：★
    

## 20-L. Expense CSV Export

家計簿をCSV出力する。

- 難易度：★
    

## 20-M. Expense CSV Import

既存CSVを読み込む。

- 難易度：★★
    

## 20-N. Receipt Memo

店名やメモを支出へ追加する。

- 難易度：★
    

## 20-O. Receipt Image

レシート画像を添付する。

- 難易度：★★〜★★★
    

## 20-P. Shared Cloud Budget

クラウド上で二人が同じ家計簿を使う。

- 難易度：★★★
    

## 20-Q. Household Dashboard

月間支出・カテゴリ・負担割合等をまとめて表示する。

- 難易度：★★
    

## 20-R. Couple Budget v1

入力、共有、集計、精算を統合する。

- 難易度：★★★
    

---

# このネタ帳の使い方

ツールを作る日は、全体を順番に消化しようとしない。

その日の状態に応じて選ぶ。

## 疲れている日

★の中から、30分程度で終わりそうなものを選ぶ。

例：

- Water Counter
    
- Launcher Random
    
- Population Half-Life Calculator
    
- Markdown Quick Memo
    
- Snack Preset Button
    
- Damage Calculator
    
- Random Enemy Generator
    

## 普通の日

★★の候補から、新しい機能や少し複雑な処理を試す。

例：

- Population Chart Viewer
    
- Obsidian Quick Capture
    
- Map Loader
    
- ChatGPT Page Timer
    
- Zenn Progress Chart
    
- Thread Personality Bot
    

## 新技術を触りたい日

★★★の候補を選ぶ。

例：

- Fitbit OAuth
    
- Android
    
- Firebase
    
- LLM API
    
- センサデータ
    
- Blender Python
    
- OCR
    

---

# ツールとして数える目安

以下を満たせば、小さくても一つのツールとして扱ってよい。

1. 単独で起動・実行できる
    
2. 入力またはユーザー操作がある
    
3. 処理結果が何らかの形で返る
    
4. READMEに「何をするものか」を1〜2文で説明できる
    

逆に、

- 色を変えただけ
    
- 配列を別ファイルへ移しただけ
    
- 文言だけ変更した
    

などは、単なる機能追加として扱ってもよい。

ただし、別技術を学ぶための独立実験になっているなら、ツールとして数えてもよい。

---

# 今後の管理方法

完成したものには通常通り番号を付ける。

例：

- `012-water-counter`
    
- `013-markdown-quick-memo`
    
- `014-simple-battle`
    

ネタ帳上の番号と、実際の完成ツール番号は一致しなくてよい。

例えば、

`9-J Simple Battle`

を次に作れば、

`012-simple-battle`

として登録する。

## 親アイデアも記録する

README等に簡単に以下を残す。

- Parent idea
    
- このツールで試したこと
    
- 将来統合できそうなもの
    

例：

> Parent idea: 2D RPG  
> HPと攻撃だけの最小戦闘システムを試す。  
> 将来的にTiny RPGへ統合可能。

---

# 方針

このネタ帳は完成させる対象ではない。

作っている途中で、

- 細かすぎる
    
- 大きすぎる
    
- 似た候補とまとめたい
    
- 新しい派生を思いついた
    
- 興味がなくなった
    

ということがあれば自由に変更する。

30個完成後も面白ければ、

**AI生成で100個ツールを作る**

へそのまま拡張する。

最重要ルールは変わらない。

**悩んでいる時間に1個作る。**

**30個完成したら勝ち。**

そして100個まで行きたくなったら、そのまま続ける。