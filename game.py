"""ゲームモジュール

ゲームモジュールは、ゲームの進行を管理するモジュール.

"""

import time
from field import Field
from block import Block
from player import Player
from user_input import UserInput
from config import Parameters
from random import randint
# import logging
import os


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (Field): フィールドのインスタンス
        blocks (list[Block]): ブロックのリスト
    """

    def __init__(self, params: Parameters) -> None:
        """ゲームクラスの初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        self.players: list[Player] = []
        self.blocks: list[Block] = []
        self.num_blocks = params.num_blocks
        self.setup(params)  # ゲームの初期設定
        self.start()  # ゲームのメインループ

    def setup(self, params: Parameters) -> None:
        """ゲームの初期設定
        ゲームの初期設定を行うメソッド．

        Args:
            params (Parameters): configのパラメータのインスタンス

        """
        field_size = params.field_size  # フィールドのサイズ
        num_blocks = params.num_blocks  # ブロックの数
        # フィールドの初期化
        self.players = [Player(1, 1)]
        self.blocks = []
        for i in range(num_blocks):
            self.blocks.append(
                Block(randint(1, field_size - 1), randint(1, field_size - 1))
                )
        self.field = Field(
            self.players,
            self.blocks,
            field_size)

    def start(self) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド．
        キー入力を受け取り，プレイヤーと敵の移動を行い，フィールドを更新する．
        ゲーム終了条件を満たした場合は終了する．

        Returns:
            str: ゲーム終了時のメッセージ (例: "Game Over!", "Game Clear!")

        """
        # ゲームのメインループ
        while True:
            #  フィールドを表示
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            self.field.display_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)

            # # blockの生成
            for _ in range(self.num_blocks):
                self.blocks.append(
                    Block(
                        randint(1, self.field.field_size - 1),
                        randint(1, self.field.field_size - 1)
                    )
                )

            # blockの移動
            for block in self.blocks:
                block.move()
                block.update_pos()

            # プレイヤーと敵の移動
            for item in self.players:
                bumped_item = self.field.check_bump(item, list(self.blocks))
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            # fieldを更新
            self.field.update_field()

            # 一定の間隔で処理を繰り返す
            # 0.3秒待つ
            time.sleep(0.3)
            # exit()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
