"""フィールドのクラスを定義するモジュール

フィールドのクラスを定義する.

"""

# from item import Item
from player import Player


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤーの位置を更新し、Fieldを表示する機能を持ちます。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (list[list[str]]): フィールドの情報
        field_size (int): フィールドのサイズ
    """

    # Fieldクラスを初期化する関数
    def __init__(
        self,
        players: list[Player],
        field_size: int = 10,
    ) -> None:
        """Fieldクラスのコンストラクタ

        Args:
            players (list[Player]): プレイヤーのリスト
            f_size (int): フィールドのサイズ

        """
        self.players = players
        self.field_size = field_size
        self.field = [
            [" " for _ in range(field_size)]
            for _ in range(field_size)
        ]
        self.update_field()

    # Fieldを更新する関数
    def update_field(self) -> list[list[str]]:
        """Fieldを更新する関数
        プレイヤーの位置を参照してFieldを更新する関数

        Returns:
            list[list[str]]: 更新されたField

        Examples:
            >>> p = Player(0, 0)
            >>> field = Field([p])
            >>> field.update_field()[0]
            ['🐯', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        """

        # fieldを一旦すべて空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = " "

        for player in self.players:
            self.field[player.now_y][player.now_x] = player.icon
        return self.field
        # pass

    # Fieldを表示する関数
    def display_field(self) -> None:
        """Fieldを表示する関数
        Fieldを表示する関数

        Examples:
            >>> p = Player(0, 0)
            >>> field = Field([p])
            >>> field.display_field()
            🐯         
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
            <BLANKLINE>
        """

        # フィールド内の最大幅を取得
        max_width = max(len(row) for row in self.field)

        for row in self.field:
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)
        # pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
