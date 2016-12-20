#!/usr/bin/env python

class Direction(object):
    left=0
    down=1
    right=2
    up=3
    def __init__(self):
        self.facing = self.left


class Me(object):
    def __init__(self, facing):
        self.orientation = Direction()
        self.orientation.facing = Direction.left if 'L' == facing else Direction.right
        self.location = [0,0]
        self.visited = []
        self.done = False

    def rotate(self, direction):
        if direction == 'L':
            self.orientation.facing = (self.orientation.facing + 1 )%4
        elif direction == 'R':
            self.orientation.facing = self.orientation.facing - 1
            if self.orientation.facing == -1:
                self.orientation.facing = self.orientation.up

    def walk(self, distance):
        """
        Returns a tuple that represents the new location.
        origin = (x,y) tuple
        orientation = a direction
        distance = an integer representing how many blocks to walk
        """
        if self.orientation.facing == Direction.left:
            #self.location[0] = self.location[0] - distance
            for i in range(distance):
                self.location[0] = self.location[0] - 1
                if tuple(self.location) not in self.visited:
                    self.visited.append(tuple(self.location))
                else:
                    print "Location already present:", self.location
                    #self.done = True
        elif self.orientation.facing == Direction.right:
            #self.location[0] = self.location[0] + distance
            for i in range(distance):
                self.location[0] = self.location[0] + 1
                if tuple(self.location) not in self.visited:
                    self.visited.append(tuple(self.location))
                else:
                    print "Location already present:", self.location
                    #self.done = True
        elif self.orientation.facing == Direction.up:
            #self.location[1] = self.location[1] + distance
            for i in range(distance):
                self.location[1] = self.location[1] + 1
                if tuple(self.location) not in self.visited:
                    self.visited.append(tuple(self.location))
                else:
                    print "Location already present:", self.location
                    #self.done = True
        elif self.orientation.facing == Direction.down:
            #self.location[1] = self.location[1] - distance
            for i in range(distance):
                self.location[1] = self.location[1] - 1
                if tuple(self.location) not in self.visited:
                    self.visited.append(tuple(self.location))
                else:
                    print "Location already present:", self.location
                    #self.done = True

def parse_input():
    """ Returns a list of the directions """
    with open('input') as f:
        line = f.readline().strip()
        return line.split(', ')

def main():
    """ Main function
    Assume we start at (0,0)
    Each direction will add to X or Y depending on L or R.

    """
    directions = parse_input()
    print(directions)


    # Process the first instruction. This will give us an orientation.
    me = Me(directions[0][0])
    me.walk(int(directions[0][1:]))

    for instr in directions[1:]:
        me.rotate(instr[0])
        me.walk(int(instr[1:]))

    print(me.location)

    print(abs(me.location[0]) + abs(me.location[1]))

if __name__ == "__main__":
    main()
