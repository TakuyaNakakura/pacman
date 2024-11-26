# Pacman Project

このプロジェクトは、Pacmanゲームの実装です。プレイヤーはキーボードを使ってキャラクターを操作し、フィールド上のアイテムを避けながら進みます。

## Requirement

- Python 3.12.5

## Installation

- 結果出力用ディレクトリを作成

```shell
mkdir result
```

- 各種モジュールのインストール

```shell
pip install -r requirements.txt
```

## Usage

- メインプログラムを実行．
  - `result/[日付][実行時刻]/` 下に実行結果とログが出力されます．

```shell
python main.py
```

- デフォルトのパラメータ設定をjson出力．

```shell
python config.py # parameters.jsonというファイルが出力される．
```

- 以下のように，上記で生成されるjsonファイルの数値を書き換えて，実行時のパラメータを指定できます．

```shell
python main.py -p parameters.json
```

- 詳しいコマンドの使い方は以下のように確認できます．

```shell
python main.py -h
```

## Parameter Settings

- 指定できるパラメータは以下の通り．

```json
{
    "param1": 0,    # ダミーのパラメータ1
    "param2": {     # ダミーのパラメータ2
        "k1": "v1",
        "k2": "v2"
    },
    "field_size": 12,  # フィールドサイズ フィールドの1辺の長さ
    "num_blocks": 6    # ブロックの数
}
```

## Directory Structure

- プロジェクトの構成は以下の通り．

```shell
.
├── 
block.py # ブロッククラス
├── 
config.py # パラメータ定義
├── 
enemy.py # 敵クラス
├── 
field.py # フィールドクラス
├── 
game.py # ゲームクラス
├── 
input_without_enter.py # エンターキーなしで入力を受け取るクラス
├── 
item.py # アイテムクラス
├── 
main.py # 実行ファイル
├── 
player.py # プレイヤークラス
├──
README.md # このREADMEファイル
├── 
requirements.txt # 必要なパッケージ
│
├──result # 結果出力ディレクトリ
│  └── 20211026_165841
├── 
user_input.py # ユーザー入力クラス
├── 
utils.py # 共有関数群
└── 
```

## How to Operate

- キーボードによる操作方法は以下の通り

```shell
・ "w" --- up
・ "a" --- left
・ "s" --- down
・ "d" --- right
```

## Classes and Functions

### `main.py`

- エントリーポイント。ゲームの初期設定とメインループを実行します。
  - `main` 関数

### `game.py`

- ゲームの進行を管理するクラス。
  - `Game` クラス
    - `start` メソッド: ゲームのメインループを実行

### `field.py`

- ゲームのフィールドを管理するクラス。
  - `Field` クラス
    - `check_bump` メソッド: アイテムの衝突判定
    - `display_field` メソッド: フィールドを表示

### `player.py`

- プレイヤーキャラクターを管理するクラス。
  - `Player` クラス
    - `get_next_pos` メソッド: 次の移動先を計算

### `enemy.py`

- 敵キャラクターを管理するクラス。
  - `Enemy` クラス
    - `get_next_pos` メソッド: 次の移動先を計算

### `item.py`

- ゲーム内のアイテムを管理するクラス。
  - `Item` クラス
    - `get_next_pos` メソッド: 次の移動先を取得
    - `update_pos` メソッド: 座標を更新

### `block.py`

- ブロックを管理するクラス。
  - `Block` クラス
    - `move` メソッド: ブロックを移動

### `user_input.py`

- ユーザー入力を管理するクラス。
  - `UserInput` クラス
    - `get_user_input` メソッド: ユーザー入力を取得

### `input_without_enter.py`

- エンターキーなしで入力を受け取るクラス。
  - `InputWithoutEnter` クラス
    - `input_without_enter` メソッド: エンターキーなしで入力を受け取る

### `config.py`

- パラメータ設定を管理するモジュール。
  - `Parameters` クラス
  - `common_args` 関数: コマンドライン引数を定義

### `utils.py`

- 便利な関数群。
  - `get_git_revision` 関数: 現在のGitリビジョンを取得
  - `setup_params` 関数: パラメータを設定
  - `dump_params` 関数: パラメータをjson出力
  - `set_logging` 関数: ログ設定
  - `update_json` 関数: jsonファイルを更新