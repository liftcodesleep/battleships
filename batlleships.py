#! /usr/bin/env python
import random

MAP_X = 10
MAP_Y = 10
MAP_X_LETTERS = "".join([chr(ord("A") + x) for x in xrange(MAP_X)])
GAME_MAP = None
DEFAULT_SPACE = "~"
fleet = {
        'O': {'length': 5},
        'B': {'length': 5},
        'D': {'length': 5},
        'E': {'length': 5},
        'Y': {'length': 5},
        'G': {'length': 5},
        }

def make_map():
    global GAME_MAP
    GAME_MAP = [[DEFAULT_SPACE for x in xrange(MAP_X)] for y in xrange(MAP_Y)]


def xlate_coords(str_coord):
    xl, yd = str_coord[0], str_coord[1:]
    x = MAP_X_LETTERS.find(xl.upper())
    y = int(yd) - 1
    if x == -1 or y < 0 or y >= MAP_Y:
        raise ValueError
    return x, y

def get_at(coords):
    return GAME_MAP[coords[1]][coords[0]]

def set_at(coords, value):
    global GAME_MAP
    if not isinstance(value, str) or len(value) != 1:
        raise ValueError
    GAME_MAP[coords[1]][coords[0]] = value

def print_map():
    print "   %s" % " ".join(MAP_X_LETTERS.upper())
    for row, data in enumerate(GAME_MAP):
        print "%02s %s" % (row + 1, " ".join(data))

def place_fleet(fleet):
    for item in fleet:
        place = place_ship(fleet[item]['length'], item)
        coord = place[0]
        direction = place[1]
        fleet[item] = {'length': fleet[item]['length'],
                       'coord': coord, 'direction': direction}

def place_ship(length, char):
    while True:
        coord = random.choice(xrange(MAP_X)), random.choice(xrange(MAP_Y))
        direction = random.choice([(0, 1), (1, 0)])
        found = False
        print coord
        if (coord[0] + (length * direction[0]) >= MAP_X or coord[1] + (length * direction[1]) >= MAP_Y):
            continue
        for i in xrange(length):
            checkpoint = ((coord[0] + (i * direction[0])), (coord[1] + (i * direction[1])))
            if get_at(checkpoint) != DEFAULT_SPACE:
                found = True
                break
        if not found:
            break
    for i in xrange(length):
        set_at(((coord[0] + i * direction[0]), (coord[1] + i * direction[1])), char)
    return coord, direction

if __name__ == '__main__':
    make_map()
    print_map()
    place_fleet(fleet)
    print_map()