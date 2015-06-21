#! /usr/bin/env python
import random
MAP_X = 10
MAP_Y = 10
MAP_X_LETTERS = "".join([chr(ord("A") + x) for x in xrange(MAP_X)])
GAME_MAP = None
DEFAULT_SPACE = "~"
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


class map:

    def make(self):
        global GAME_MAP
        GAME_MAP = [
            [DEFAULT_SPACE for x in xrange(MAP_X)] for y in xrange(MAP_Y)]

    def xlate_coords(self, str_coord):
        xl, yd = str_coord[0], str_coord[1:]
        x = MAP_X_LETTERS.find(xl.upper())
        y = int(yd) - 1
        if x == -1 or y < 0 or y >= MAP_Y:
            raise ValueError
        return x, y

    def get_at(self, coords):
        return GAME_MAP[coords[1]][coords[0]]

    def set_at(self, coords, value):
        global GAME_MAP
        if not isinstance(value, str) or len(value) != 1:
            raise ValueError
        GAME_MAP[coords[1]][coords[0]] = value

    def print_(self):
        print "   %s" % " ".join(MAP_X_LETTERS.upper())
        for row, data in enumerate(GAME_MAP):
            print "%02s %s" % (row + 1, " ".join(data))


class boats:

    def place(self, fleet):
        for item in fleet:
            place = place_ship(fleet[item]['length'], item)
            coord = place[0]
            direction = place[1]
            fleet[item] = {'length': fleet[item]['length'],
                           'coord': coord, 'direction': direction}

    def make(self, length, char):
        while True:
            coord = random.choice(xrange(MAP_X)), random.choice(xrange(MAP_Y))
            direction = random.choice([(0, 1), (1, 0)])
            found = False
            print coord
            if (coord[0] + (length * direction[0]) >=
                    MAP_X or coord[1] + (length * direction[1]) >= MAP_Y):
                continue
            for i in xrange(length):
                checkpoint = (
                    (coord[0] + (i * direction[0])), (coord[1] + (i * direction[1])))
                if get_at(checkpoint) != DEFAULT_SPACE:
                    found = True
                    break
            if not found:
                break
        for i in xrange(length):
            set_at(
                ((coord[0] + i * direction[0]), (coord[1] + i * direction[1])), char)
        return coord, direction

if __name__ == '__main__':
    map.make(self)
    map.print_(self)
    boats.place(self, fleet)
    map.print_(self)
