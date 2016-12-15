#!/usr/bin/env python

def get_inputs():
    with open('input') as f:
        return [x.split() for x in f.readlines()]

def do_sum(sides, sum_set):
    r = 0
    for s in sum_set:
        r = r + sides[s]
    return r

def validate_triangle(triangle):
    triangle = [int(x) for x in triangle]
    sides = set([0, 1, 2])
    if (triangle[0] < triangle[1] + triangle[2] and
        triangle[1] < triangle[0] + triangle[2] and 
        triangle[2] < triangle[0] + triangle[1]):
        return True
#    for i in range(0, 3):
#        s = sides - set([i])
#        if (triangle[i] > do_sum(triangle, s)):
#            return False
    return False

def main():
    count = 0
    triangles = get_inputs()
    print "Total triangles: ", len(triangles)
    for triangle in get_inputs():
        if validate_triangle([x.strip() for x in triangle]):
            count = count + 1
    print count


if __name__ == "__main__":
    main()
