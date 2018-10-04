#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  Program drukuje wypełniony prostokąt o bokach podanych przez
#  użytkownika za pomocą podanego znaku


def main(args):
    
    a = int(input("Podaj długość 1 boku: "))
    b = int(input("Podaj długość 2 boku: "))
    
    for i in range(a):
        for j in range(b):
            print("#", end='')
        print()   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
