
# create by fuji
"""
パックマン本体の設定
"""
from item import Item
#from user_input import input

class Player(Item):
    """プレイヤークラス
    Itemを継承して作成したプレイヤークラス.
    入力から移動方向を受け取って移動しようとする方向を計算するメソッドと
    マップから移動して良いと許可が出た時に呼び出される座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """
    def __init__(self,x,y):
        pass

    def next_position(self,dir: tuple[int,int]):
        """
        itemクラスから継承
        user_inputから次の自分の位置を取得

        arg:
         移動方向をtupleで取得
        return:
            移動先の座標
        """
    
