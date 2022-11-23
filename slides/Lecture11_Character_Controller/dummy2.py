class Player:
    name = 'Player'

    def __init__(self):
        self.x = 100

    def print(self):
        print(self.x)

player = Player()
player.print()
print(Player.name)

Player.print(player)