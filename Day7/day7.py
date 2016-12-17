#!/usr/bin/env python

def extract_hypernet(in_str):
    i1 = in_str.find("[")
    i2 = in_str.find("]")
    if i1 == -1 or i2 == -1:
        return (in_str, None, None)
    else:
        # Return first, last, and hypernet
        return (in_str[:i1], in_str[i2+1:], in_str[i1+1:i2])

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
    #print "string of length " ,len(in_str)," range:", len(in_str)-3
#    print in_str
    for i in range(len(in_str)-3):
        #print "Checking for ABBA:", in_str[i:i+2], in_str[i+3:i+1:-1]
        # Needs to meet ABBA but also can't all be the same character
        print in_str[i:i+2], in_str[i+3:i+1:-1]
        if (in_str[i:i+2] == in_str[i+3:i+1:-1] and
            in_str[i:i+2] != in_str[i+2:i+4]):
#            print "Found ABBA:", in_str[i:i+4]
            return True
    return False


def parse_input():
    inputs = []
    with open('input.txt') as f:
        for line in f.readlines():
            row = {}
            row['hypernet'] = []
            row['ip'] = []
            in_str = line
            last = in_str
            while last is not None:
                first, last, hypernet = extract_hypernet(in_str)
                row['ip'].append(first)
                if hypernet is not None:
                    row['hypernet'].append(hypernet)
                if last is not None:
                    in_str = last
            print line, ":", row
            inputs.append(row)
    for i in inputs:
        for x in i['ip']:
            if "[" in x or "]" in x:
                print x
        for x in i['hypernet']:
            if "[" in x or "]" in x:
                print x
    return inputs

def check_abba_list(abba_list):
    for i in abba_list:
        if check_ABBA(i):
            return True

def main():
    count = 0
    inputs = parse_input()
    for inp in inputs:
#        print "ip: ", inp['ip'], "hypernets: ", inp['hypernet']
        #if check_abba_list(inp['ip']) and not check_abba_list(inp['hypernet']):
        if check_abba_list(inp['ip']) and not check_abba_list(inp['hypernet']):
            count = count + 1
    print count


if __name__ == "__main__":
    main()
