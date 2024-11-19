from item import Item
import random


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
        self.now_y = int(random.random()) % 10
        self.now_x = 10

    def update_pos(self, stuck: bool = False) -> tuple[int, int]:
        """
        x軸を一つずらす関数

        Return:
            tuple[int, int]
        """
        if stuck:
            del self
        self.next_x = self.now_x - 1
        self.next_y = self.now_y
        return (self.next_x, self.next_y)
