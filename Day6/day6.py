#!/usr/bin/env python

def process_input():
    inputs = []
    with open('input.txt') as f:
        lines = f.readlines()
        # First let's generate the empty list
        for i in range(len(lines[0])):
            inputs.append("")
        for l in lines:
            for i in range(len(l)):
                inputs[i] += l[i]
    return inputs

def main():
    columns = process_input()

    from collections import defaultdict
    for c in columns:
        d = defaultdict(lambda: 0)
        for x in c:
            d[x] = d[x] + 1
        l = d.items()
        l.sort(lambda x,y: cmp(x[1],y[1])*-1)
        print l[0][0]

if __name__ == "__main__":
    main()
