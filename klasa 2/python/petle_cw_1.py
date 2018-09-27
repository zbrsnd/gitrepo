#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pentle_cw_1.py
#  
# Program podaje liczby podane przez użytkownika, do momentu kiedy ich suma nie przekroczy 75. Na koniec drukuje sumę.


def main(args):
    suma = 0
    while suma <= 75:
        liczba = int(input("Podaj liczbę: "))
        suma = suma + liczba
    print("Suma liczb:", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
