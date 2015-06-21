import mapset
import random


class Game:

    def __init__(self):
        self.p1 = mapset.Player(raw_input('Player 1\'s name?: '))
        self.p2 = mapset.Player(raw_input('Player 2\'s name?: '))
        self.counter = random.choice([0, 1])
        self.names = [self.p1.name, self.p2.name, ]
        self.players = [self.p1, self.p2]

    def current(self):
        return (self.counter % 2)

    def run(self):
        print 'Game between ' + self.p1.name + ' and ' + self.p2.name + '! \nStart!'
        return self.counter

    def turn(self):
        cpn = self.names[self.current()]
        cp = self.players[self.current()]
        print 'It\'s ' + str(cpn) + '\'s turn!'
        cp.random_shot()
        #cp.boatsmap.shoot(cp.boatsmap.xlate_coords(raw_input('Where would you like to shoot?: ')))
        self.counter += 1

if __name__ == '__main__':
    test = Game()
    test.run()
    while True:
        test.turn()
