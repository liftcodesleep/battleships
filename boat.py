#! /usr/bin/env python


class Boat:

    def __init__(self, char, length):
        self.char = char
        self.length = length
        self.body = [0 for i in xrange(length)]
        self.coord = None
        self.direction = None

    def place(self, coord, direction):
        self.coord = coord
        self.direction = direction

    def shot_at(self, coord):
        for i in xrange(self.length):
            if ((self.coord[0] + i * self.direction[0]),
                    (self.coord[1] + i * self.direction[1])) == coord:
                self.body[i] = 1
                return True
        return False

    def is_sunk(self):
        for i in self.body:
            if i == 0:
                return False
        return True

    # Going to also need methods for recording shots/sunken-ness

if __name__ == '__main__':
    pass
