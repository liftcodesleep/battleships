import gamemap
import random


class Player:

    def __init__(self, name):
        self.name = name
        self.boatsmap = gamemap.GameMap()
        self.shotsmap = gamemap.GameMap()
        fleets = [{
            'O': {'length': 2},
            'B': {'length': 3},
            'D': {'length': 3},
            'E': {'length': 4},
            'G': {'length': 5},
        },
            {
            'O': {'length': random.choice(range((5) + 1))},
            'Q': {'length': random.choice(range((5) + 1))},
            'P': {'length': random.choice(range((5) + 1))},
            'G': {'length': random.choice(range((5) + 1))},
            'D': {'length': random.choice(range((5) + 1))},
        }]
        fleet = random.choice(fleets)
        flee = {'o': {'length': 1}}
        self.boatsmap.place_fleet(fleet)
    def get_target(self):
        return self.boatsmap.xlate_coords((raw_input('Where would you like to shoot? ')))

    def turn(self):
        print "%s\'s turn!" % (self.name)
        print 'boats'
        self.boatsmap.display()
        print 'shots'
        self.shotsmap.display()
        target = self.get_target()
        self.shotsmap.record_shot(target)
        return target
class AI:

    def __init__(self, name):
        self.name = name
        self.boatsmap = gamemap.GameMap()
        self.shotsmap = gamemap.GameMap()
        fleets = [{
            'O': {'length': 2},
            'B': {'length': 3},
            'D': {'length': 3},
            'E': {'length': 4},
            'G': {'length': 5},
        },
            {
            'O': {'length': random.choice(range((5) + 1))},
            'Q': {'length': random.choice(range((5) + 1))},
            'P': {'length': random.choice(range((5) + 1))},
            'G': {'length': random.choice(range((5) + 1))},
            'D': {'length': random.choice(range((5) + 1))},
        }]
        fleet = random.choice(fleets)
        flee = {'o': {'length': 1}}
        self.boatsmap.place_fleet(fleet)

    def display(self):
        self.boatsmap.display()
        self.shotsmap.display()

    def get_target(self):
        return self.boatsmap.rand_coord()

    def turn(self):
        print "%s\'s turn!" % (self.name)
        print 'boats'
        self.boatsmap.display()
        print 'shots'
        self.shotsmap.display()
        target = self.get_target()
        self.shotsmap.record_shot(target)
        return target



if __name__ == '__main__':
    thing = AI()
    thing.display()
