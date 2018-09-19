#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Program pobiera 3 liczby całkowite i wyświetla liczbę największą

def maks(a, b, c):
    
    maks = a
    if b > maks:
        maks = b
    if c > maks:
        maks = c
    
    pass
    return maks 


def main(args):
    
    a = int(input('Podaj 1. liczbę: '))
    b = int(input('Podaj 2. liczbę: '))
    c = int(input('Podaj 3. liczbę: '))
    
    #if b <= a >= c: #3 1 2
    #   print(a, 'jest największa')
    #elif c <= b >= a:
    #    print(b, 'jest największa')
    #else:
    #    print(c, 'jest największa')
   
    assert(maks)
    
    
    #if warunek --> egezkwowanie warunku
    #elif = else + if --> sprawdza kolejne warunki
    #else 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
