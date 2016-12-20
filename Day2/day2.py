#!/usr/bin/env python

class Keypad(object):
    def __init__(self):
        self.pad = [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
        self.pad = [['1'],
                   ['2','3','4'],
                   ['5','6','7','8','9']
                   ['a','b','c']
                   ['d']]
        self.row = 1
        self.column = 1

        print self.pad[0]
        print self.pad[1]
        print self.pad[2]

        print len(self.pad)
        print len(self.pad[0])

    def follow(self, line):
#        print "Starting at: ", self.pad[self.row][self.column]
        for c in line:
            if c == 'U':
                self.row = max(self.row - 1, 0)
            elif c == 'D':
                self.row = min(self.row + 1, 2)
            elif c == 'R':
                self.column = min(self.column + 1, 2)
            elif c == 'L':
                self.column = max(self.column - 1, 0)
            else:
                print "Bad direction", c
        print "(%d, %d):" %(self.row, self.column), self.pad[self.row][self.column]

def parse_input():
    """ Returns a list of the directions """
    with open('input') as f:
        return f.readlines()

def main():
    directions = parse_input()

    keypad = Keypad()

    for instr in directions:
        keypad.follow(instr.strip())

if __name__ == "__main__":
    main()
