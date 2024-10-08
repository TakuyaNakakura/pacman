"""フィールドのクラスを定義するモジュール

フィールドのクラスを定義する.

"""

from item import Item
from player import Player


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤーの位置を更新し、Fieldを表示する機能を持ちます。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    # Fieldクラスを初期化する関数
    def __init__(
        self,
        players: list[Player],
        f_size: int = 10,
    ) -> None:
        """Fieldクラスのコンストラクタ

        Args:
            players (list[Player]): プレイヤーのリスト
            f_size (int): フィールドのサイズ
        """
        pass

    def update_field(self) -> list[list[str]]:
        """Fieldを更新する関数
        プレイヤーの位置を参照してFieldを更新する関数

        Returns:
            list[list[str]]: 更新されたField

        Examples:

        """

        pass

    def display_field(self) -> None:
        """Fieldを表示する関数
        Fieldを表示する関数

        Examples:

        """
        pass
