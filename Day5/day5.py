#!/usr/bin/env python

import md5

def main():
    door_id = "abbhdwsy"
    index = 0

    s = md5.new(door_id + str(index)).hexdigest()
    password = ""
    for i in range(0,8):
        while not s.startswith("00000"):
            index = index + 1
            s = md5.new(door_id + str(index)).hexdigest()
        print s
        password = password + s[5]
        index = index + 1
        s = md5.new(door_id + str(index)).hexdigest()
    print password

if __name__ == "__main__":
    main()
