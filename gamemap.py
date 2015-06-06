#! /usr/bin/env python

import boat
import random

class GameMap:

    def __init__(self):
        self.empty = "~"
        self.max_x = 10
        self.max_y = 10
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

    def display(self):
        print "   %s" % " ".join(self.x_labels.upper())
        for row, data in enumerate(self.map):
            print "%02s %s" % (row + 1, " ".join(data))

     def place_fleet(self, fleet):
         # code here to place fleet
         pass
            
if __name__ == "__main__":
    map = GameMap()
    map.display()
    fleets = [{
        'O': {'length': 5},
        'B': {'length': 5},
        'D': {'length': 5},
        'E': {'length': 5},
        'Y': {'length': 5},
        'G': {'length': 5},
    },
    {
        'O': {'length': random.choice(range(11))},
        'Q': {'length': random.choice(range(11))},
        'P': {'length': random.choice(range(11))},
        'G': {'length': random.choice(range(11))},
        'D': {'length': random.choice(range(11))},
    }]
    fleet = random.choice(fleets)
    map.place_fleet(fleet)
