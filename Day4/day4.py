#!/usr/bin/env python

def get_inputs():
    sector_list = []
    with open('input.txt') as f:
        for x in f.readlines():
            row = []
            x = x.split("-")
            row.append("".join(x[:-1]))
            x = x[-1].split("[")
            row.append(int(x[0]))
            x = x[-1].split("]")
            row.append(x[0])
            sector_list.append(row)
    return sector_list

def compute_checksum(enc_name):
    # count the number of each letter
    from collections import defaultdict
    d = defaultdict(lambda: 0)
    for c in enc_name:
        d[c] = d[c] + 1
    s = d.items()
    s.sort(cmp=lambda x,y: cmp(x[0],y[0]))
    s.sort(cmp=lambda x,y: cmp(x[1], y[1])*-1)
    return "".join(x[0] for x in s[:5])

def main():
    sectors = get_inputs()
    total = 0
    for s in sectors:
        if compute_checksum(s[0]) == s[2]:
            total = total + s[1]
    print total

if __name__ == "__main__":
    main()
