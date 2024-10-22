"""ゲームモジュール

ゲームモジュールは、ゲームの進行を管理するモジュール.

"""

import time
from field import Field
from player import Player


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (Field): フィールドのインスタンス
    """
