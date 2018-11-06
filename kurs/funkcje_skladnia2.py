#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia2.py

def mnoz(a, b):
    print(a * b)

def mnoz2(*args):  # zmienna lista argumentów
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)
    

def wylicz(imie1='adam', imie2='ewa', **kwargs): # słownik zmiennej długości
    print(imie1)
    print(imie2)
    for k, v in kwargs.items():
        print('{} {}'.format(k,v))
        
######## TYPY ARGUMENTÓW W FUNKCJACH
# POZYCYJNE / wymagane
# NAZWANE / wymagane
# DOMYŚLNE / niewymagane
# ZMIENNEJ DŁUGOŚCI: listy, słowniki


    

def main(args):
    mnoz(4, 6)
    mnoz2(1, 2, 3, 4, 5, 6, 7, 8)
    wylicz(imie2='ola', imie3='piotr', imie4='alfons')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
