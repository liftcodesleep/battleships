#! /usr/bin/env python

class Boat:
    
    def __init__(self, length):
        self.length = length
        self.body = [0 for i in xrange(length)]
        self.coords = None
        
    def place(self, coords):
        self.coords = coords
        
    def is_afloat(self):
        pass

    # Going to also need methods for recording shots/sunken-ness
    
if __name__ == '__main__':
    pass
