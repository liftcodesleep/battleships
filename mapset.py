import gamemap
import random

class Mapset:
    def __init__(self):
        self.boats = gamemap.GameMap()
        self.shots = gamemap.GameMap()
        fleets = [{
            'O': {'length': 2},
            'B': {'length': 3},
            'D': {'length': 3},
            'E': {'length': 4},
            'G': {'length': 5},
        },
        {
            'O': {'length': random.choice(range(6))},
            'Q': {'length': random.choice(range(6))},
            'P': {'length': random.choice(range(6))},
            'G': {'length': random.choice(range(6))},
            'D': {'length': random.choice(range(6))},
        }]
        fleet = random.choice(fleets)
        self.boats.place_fleet(fleet)

    def random_shot(self):
        at = self.boats.rand_coord()
        if self.boats.shoot(at):
            return at
        return False


    def when_shot(self):
        origin = self.random_shot()
        if origin:
            x, y = origin
            targets = [((x + 1), y), ((x - 1), y), (x, (y + 1)), (x, (y - 1)),]
            self.boats.shoot(random.choice(targets))


    def display(self):
        self.boats.display()
        self.shots.display()

if __name__ == '__main__':
    thing = Mapset()
    thing.when_shot()
    thing.when_shot()
    thing.when_shot()
    thing.when_shot()
    thing.when_shot()
    thing.when_shot()
    thing.display()
