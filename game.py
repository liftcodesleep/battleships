import player
import random


class Game:

    def __init__(self, name, name2, fleet):
        self.players = [player.Player(name), player.Player(name2)]
        self.counter = random.choice([0, 1])

    def current(self):
        return (self.counter % 2)

    def run(self):
        print 'Game between %s and %s! \nStart!' %(self.players[0].name, self.players[1].name)
        turn_counter = 0
        while True:
            print '------------------------------ \n------------------------------'
            print 'It\s turn %d' % (turn_counter)
            self.turn()
            turn_counter += 1

    def turn(self):
        cp = self.players[self.current()]
        np = self.players[self.current() - 1]
        print 'It\'s %s\'s turn!' % (cp.name)
        print 'boats'
        cp.boatsmap.display()
        print 'shots'
        cp.shotsmap.display()
        if self.current() == 0:
            #shot = raw_input('Where would you like to shoot?: ')
            #target = cp.boatsmap.xlate_coords(shot)
            target = cp.shotsmap.rand_coord()
        else:
            target = np.shotsmap.rand_coord()
        np.boatsmap.shoot(target)
        cp.shotsmap.record_shot(target)
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
    test.run()
