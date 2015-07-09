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

    def display(self):
        self.boatsmap.display()
        self.shotsmap.display()

if __name__ == '__main__':
    thing = Mapset()
    thing.random_shot()
    thing.random_shot()
    thing.random_shot()
    thing.random_shot()
    thing.random_shot()
    thing.random_shot()
    thing.display()
