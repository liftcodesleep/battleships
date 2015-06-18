import player
class Game:
    def __init__(self):
        self.p1 = player.Player('1')
        self.p2 = player.Player('2')

    def run(self):
        raw_input('Give a coordinate: ')