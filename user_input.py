

class Input():
    """
    キーボードから入力を受け取るクラス
    """
    def get_user_input(self) -> tuple[int,int]:
        """
        ユーザーの入力を受け取り、移動方向をtupleで返すプログラム

        return:
            tuple[int,int] 右(1,0)左(-1,0)上(0,-1)下(0,1) 
        """