from item import Item


class Block(Item):
    """
    Blockクラス
    アイテムの位置とアイコンを管理するクラス

    Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン
    """
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "■"
        self.now_y = y
        self.now_x = x

    def move(self, stuck: bool = False) -> tuple[int, int]:
        """
        x軸を一つずらす関数

        Return:
            tuple[int, int]
        """
        if self.now_x - 1 <= 0:
            self.status = False
        self.next_x = self.now_x - 1
        self.next_y = self.now_y
        return (self.next_x, self.next_y)
