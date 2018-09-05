#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby
    # print("Wylosowano:", liczba)
    # pobieranie danych od użytkownika
    if liczba > 5:
        print("Liczba jest większa od 5")
    else:
        print("Liczba jest mniejsza od 5")
    for i in range(3):
        print("Próba:", i + 1)
        odp = input('Podaj liczbę od 1 do 10')
        print("Podano liczbę:", odp)

        if liczba == int(odp): # porównywanie liczby z odpowiedzią
            print("Odgadłeś/aś liczbę!")
            break # przerwanie działania pętli
        elif i == 2:
            print("Wylosowano:", liczba)
        else:
            print("Nie odgadłeś liczby.",)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
