#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py

def main(args):
    #a = 0 #inicjacja zmiennej
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    
    suma = float(a) + float(b)
    roznica = float(a) - float(b)
    iloraz= float(a) / float(b)
    iloczyn = float(a) * float(b)
    
    
    print('Suma:', suma)
    print('Różnica:', roznica)
    print('Iloraz:', iloraz)
    print('Iloczyn:', iloczyn)
    
   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
