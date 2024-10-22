from item import Item
import random


class Enemy(Item):
    """
    itemクラスを継承する
    エネミーを動かす関数。
    ランダム関数で0,1をランダムに出力し移動方向を決定

    attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """
    def __init__(self, x, y):
        super().__init__(x, y)

    def get_next_pos(self, x, y) -> tuple[int, int]:
        """
        ランダム関数にて移動方向を入力、次の座標を返すメゾット
        ２値をランダムに出力し、移動方向を返す。

        return:
            移動方向 tuple[int, int]

        """
        position = {(0,0),(1,0),(0,1)}
        dir = random.choice(position)
        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)

if __name__ == "__main__":
    import doctest
    doctest.testmod()