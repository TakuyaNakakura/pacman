"""Blockクラスを定義するモジュール

    Blockクラスは

"""

from item import Item
import doctest


class Block(Item):
    """
    Blockクラス
    アイテムの位置とアイコンを管理するクラス

    Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン
    """
