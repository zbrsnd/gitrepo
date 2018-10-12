#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
#

def euklides(a,b):
    
    while a != b:
        if a > b:
            a = a -b
        else:
            b = b - a
            
    return a


def nww(a,b):
    
    pass


def main(args):
    
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    print("NWD({}, {}) = {}".format(a, b, euklides(a,b)))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
