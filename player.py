
# create by fuji
class player:
    def __init__(self):
        player.x = 0
        player.y = 0
        player.HP = 5

    def move(self,moves):
        if moves == 0:
            player.x += 1
        if moves == 1:
            player.x += -1
        if moves == 2:
            player.y += 1
        if moves == 1:
            player.y += -1
        
    def damage(self):
        player.HP -= 1
