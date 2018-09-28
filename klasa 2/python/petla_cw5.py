#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_cw2.py
#  
# DANE WEJSCIOWE:
# liczby dodatnie podawane przez uzytkownika
# DANE WYJSCIOWE:   
# suma liczb podanych przez uzytkownika
# WARUNKI DZIAŁANIA:
# program musi zapewnić poprawność danych
# program konczy dzialanie po wprowadzeniu wartosci 0
#print(i, "", end="")



def pobierzMiesiac():
    
    """
    napisz program ktory wczytuje z klawiatury poprawny numer miesiaca
    mozliwe sa maksymalnie trzy proby
    wydrukuj podany numer oraz nazwy miesiaca
    """
    
    nazwy = ['', 'styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien'



def main(args):

    suma = 0
    liczba = -1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))
        while liczba < 0:
            liczba = int(input("Błędne dane. Podaj liczbę: "))
        suma += liczba
    
    print("Suma:", suma)    
    
    return 0



def main(args):

    suma = 0
    liczba = -1
    
    while liczba != 0:
        liczba = int(input("Podaj liczbę: "))
        if liczba < 0:
            print("Błędne dane!", end="")
        else:
            suma += liczba
    
    print("Suma:", suma)    
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
