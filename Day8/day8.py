#!/usr/bin/env python

from __future__ import print_function

class LCD(object):
    # 50 cols x 6 rows
    display = [
            [False]*50,
            [False]*50,
            [False]*50,
            [False]*50,
            [False]*50,
            [False]*50]

    def __init__(self, rows, cols):
        print("Initializing array of %d rows by %d columns" %(len(self.display), len(self.display[0])))
        self.display = []
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            self.display.append([False]*cols)

    def get_lit(self):
        count = 0
        for row in self.display:
            count = count + row.count(True)
        return count

    def __str__(self):
        d = ""
        for i in self.display:
            d = d + " ".join(['T' if x else ' ' for x in i]) + "\n"
        return d

    def rect(self, A, B):
        """ Turns on all pixels in a rectangle A wide and B tall starting from upper left """
        print("Turning on rectangle %d by %d" %(A, B))
        for i in range(B):
            self.display[i][:A] = [True]*A

    def rotate_row(self, A, B):
        """
        shifts all of the pixels in row A (0 is the top row) right by B pixels.
        Pixels that would fall off the right end appear at the left end of the row.
        """
        print("Shifting row %d by %d pixels" %(A, B))
        self.display[A] = self.display[A][len(self.display[A])-B:] + self.display[A][:len(self.display[A])-B]

    def rotate_col(self, A, B):
        """ Shifts column A down by B pixels """
        print("Shifting column %d by %d pixels" %(A, B))
        # I think we could probably use zip for this?
        o_col = [x[A] for x in self.display]
        o_col = o_col[len(o_col)-B:] + o_col[:len(o_col)-B]
        for i in range(self.rows):
            self.display[i][A] = o_col[i]

def process_input():
    with open('input.txt') as f:
        return [x.strip() for x in f.readlines()]

def main():
    lcd = LCD(6,50)
    for instr in process_input():
        if 'rect' in instr:
            instr = instr.split()[-1].split('x')
            lcd.rect(int(instr[0]),int(instr[1]))
        else:
            a = int(instr[instr.find('=')+1:].split()[0])
            b = int(instr.split(' by ')[-1])
            if 'row' in instr:
                lcd.rotate_row(a, b)
            elif 'column' in instr:
                lcd.rotate_col(a, b)
    print("Number of LEDs lit: ", lcd.get_lit())
    print(lcd)

if __name__ == "__main__":
    main()
