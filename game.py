import player
import random


class Game:

    def __init__(self, name, name2, fleet):
        self.players = [player.Player(name), player.AI(name2)]
        self.counter = random.choice([0, 1])

    def current(self):
        return (self.counter % 2)

    def run(self):
        print 'Game between %s and %s! \nStart!' %(self.players[0].name, self.players[1].name)
        turn_counter = 0
        while True:
            print '------------------------------ \n------------------------------'
            print 'Turn %d' % (turn_counter)
            self.turn()
            turn_counter += 1

    def turn(self):
        cp = self.players[self.current()]
        np = self.players[self.current() - 1]
        target = cp.turn
        np.boatsmap.shoot(target)
        self.counter += 1


if __name__ == '__main__':
    fleet = {
        'O': {'length': 2},
        'B': {'length': 3},
        'D': {'length': 3},
        'E': {'length': 4},
        'G': {'length': 5},
        }
    test = Game('Player 1', 'Computer', fleet,)
    while True:
        test.run()
