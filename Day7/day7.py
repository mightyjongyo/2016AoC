#!/usr/bin/env python

def check_ABBA(in_str):
    """
    A string meets ABBA if it, well, looks like abba,
    e.g. character pair + reversed character pair
    """
    # Don't really like this approach but let's do a rolling window.
    # Start with the first 4 characters, and move the window, checking for ABBA

    # Obviously if the strlen is < 4 there aren't enough characters to check.
    if len(in_str) < 4:
        return False

    # We want to check everything, but only up to n-3
    # since that will cover the last set of 4
    print "string of length " ,len(in_str)," range:", len(in_str)-3
    for i in range(len(in_str)-2):
        #print "Checking for ABBA:", in_str[i:i+2], in_str[i+3:i+1:-1]
        # Needs to meet ABBA but also can't all be the same character
        if (in_str[i:i+2] == in_str[i+3:i+1:-1] and
            in_str[i:i+2] != in_str[i+2:i+4]):
            print "Found ABBA:", in_str[i:i+4]
            return True
    return False


def parse_input():
    inputs = []
    with open('input.txt') as f:
        for line in f.readlines():
            #Fuck, we can have multiple hypernet sequences...
            row = []
            #row.append(line.split("[")[0])
            row.append(line.split("[")[0] + line.split("[")[1].split("]")[1].strip())
            row.append(line.split("[")[1].split("]")[0])
            r#ow.append(line.split("[")[1].split("]")[1].strip())
            inputs.append(row)
    return inputs

def main():
    count = 0
    inputs = parse_input()
    for inp in inputs:
        if check_ABBA(inp[0]) and not check_ABBA(inp[1]):
#        if (check_ABBA(inp[0]) or check_ABBA(inp[2])) and not check_ABBA(inp[1]):
            count = count + 1
    print count


if __name__ == "__main__":
    main()
