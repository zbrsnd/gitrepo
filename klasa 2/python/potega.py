#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# Obliczanie potęgi liczby naturalnej.


def potega_it(a, n):
    
    wynik = 1
    
    for i in range(n):
        wynik = wynik * a
        #print(wynik)
        
    return wynik   
    
    pass
def main(args):
    
    #a = int(input("Podaj podstawę potęgi")
    #n = int(input("Podaj wykładnik potęgi")
    a, n = 0, 2
    print("Podstawa {} do potęgi {} wynosi {} ".
           format(a,n,potega_it(a,n)))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
