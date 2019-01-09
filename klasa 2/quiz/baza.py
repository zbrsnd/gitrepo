#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from modele import *
import csv

def czy_jest(plik):
    """ funkcja sprawdza czy plik istnieje na dysku"""
    if not os.path.isfile(plik):
        print("TY OŚLE!Nie ma pliku {} na dysku!".format(plik))
        return False
    return True


def dane_z_pliku(nazwa_pliku, separator=','):
    """ domyślny separator -> przecinek, chyba że coś innego jest podane"""
    dane = []  # pusta lista na dane
    if not czy_jest(nazwa_pliku):
        return dane
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # usunięcie białych znaków
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane

def dodaj_dane(dane):
    
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0) # usuwanie pierwszego rekordu z listy
        
        wpisy = dane_z_pliku(plik + '.csv', ';')
        model.insert_many(wpisy, fields=pola).execute()

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Kategoria, Pytanie, Odpowiedz])
    
    dane = {
        Kategoria: 'kategorie',
        Pytanie: 'pytania',
        Odpowiedz: 'odpowiedzi',
    }
    dodaj_dane(dane)
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
