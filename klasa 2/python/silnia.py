#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# Obliczanie silni liczby naturalnej.


def silnia_it(n):
    """
    Funkcjca oblicza silnięliczby naturalnej
    n! = n*(n-1)
    """
    wynik = 1

    for i in range(1,n+1):
        wynik = n * (n-1)
        #print(wynik)
        
    return wynik   
    
    pass
def main(args):
    
    #a = int(input("Podaj podstawę potęgi")
    #n = int(input("Podaj wykładnik potęgi")
    n =  int(input("Podaj podstawę silni: "))
    print("{}! wynosi {} ".
           format(n,silnia_it(n)))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
