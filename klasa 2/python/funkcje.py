#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py

#zasięg zmiennych: lokalny, globalny

def dodaj(a, b):
    return(a + b)

def odejmij(a, b):
    return(a - b)
    
def pomnoz(a, b):
    return(a * b)
    
def podziel(a, b):
    return(a / b)
    
            
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
    
    
    print('Suma:', dodaj(a, b))
    print('Różnica:', odejmij(a, b))
    print('Iloraz:', podziel(a, b))
    print('Iloczyn:', pomnoz(a, b))
    
    
   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
