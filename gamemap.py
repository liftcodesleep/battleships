#! /usr/bin/env python

import boat
import random

class GameMap:

    def __init__(self):
        self.empty = "~"
        self.shat = 'X'
        self.max_x = 10
        self.max_y = 10
        self.fleet = []
        self.x_labels = "".join([chr(ord("A") + x)
                                for x in xrange(self.max_x)])
        self.y_labels = range(1, self.max_y + 1)
        self.map = [[self.empty for x in xrange(
                     self.max_x)] for y in xrange(self.max_y)]

    def xlate_coords(self, str_coord):
        xl, yd = str_coord[0], str_coord[1:]
        x = self.x_labels.find(xl.upper())
        y = int(yd) - 1
        if x == -1 or y < 0 or y >= self.max_y:
            raise ValueError
        return x, y

    def get_at(self, coords):
        return self.map[coords[1]][coords[0]]

    def set_at(self, coords, value):
        if not isinstance(value, str) or len(value) != 1:
            raise ValueError
        self.map[coords[1]][coords[0]] = value

    def is_empty(self, coords):
        return self.map[coords[1]][coords[0]] == self.empty

    def rand_coord(self):
        return (random.choice(xrange(self.max_x)), random.choice(xrange(self.max_y)))

    def display(self):
        print "   %s" % " ".join(self.x_labels.upper())
        for row, data in enumerate(self.map):
            print "%02s %s" % (row + 1, " ".join(data))

    def place_boat(self, boat):
        while True:
            coord = random.choice(xrange(self.max_x)), random.choice(xrange(self.max_y))
            direction = random.choice([(0, 1), (1, 0)])
            found = False
            if (coord[0] + (boat.length * direction[0]) >= self.max_x or coord[1] + (boat.length * direction[1]) >= self.max_y):
                continue
            for i in xrange(boat.length):
                checkpoint = ((coord[0] + (i * direction[0])), (coord[1] + (i * direction[1])))
                if self.get_at(checkpoint) != self.empty:
                    found = True
                    break
            if not found:
                break
        for i in xrange(boat.length):
            self.set_at(((coord[0] + i * direction[0]), (coord[1] + i * direction[1])), boat.char)
        boat.place(coord, direction)
        return coord, direction

    def place_fleet(self, fleet):
        for k, v in fleet.items():
            ba = boat.Boat(k, v['length'])
            coord, direction = self.place_boat(ba)
            self.fleet.append(ba)



    def shoot(self, coord,):
        for boat in self.fleet:
            if boat.shot_at(coord):
                print 'hit'
                self.set_at(coord, self.shat)
                if boat.is_sunk():
                    print 'You sunk the %s' % boat.char
                return True
        print 'miss'
        self.set_at(coord, self.shat)
        return False

if __name__ == "__main__":
    map = GameMap()
    map.display()
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
    map.place_fleet(fleet)
    map.display()
