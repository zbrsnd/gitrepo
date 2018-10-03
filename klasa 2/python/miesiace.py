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



def main(nazwa):
    
    """
    napisz program ktory wczytuje z klawiatury poprawny numer miesiaca
    mozliwe sa maksymalnie trzy proby
    wydrukuj podany numer oraz nazwy miesiaca
    """
    
    nazwa = ['', 'styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
    a = 3
    while a > 0:
        a -= 1
        miesiac = int(input("podaj numer miesiąca: "))
        if miesiac > 12 or miesiac < 1 :
            print("Błędne dane! Wpisz raz: ")
        else:
            print (nazwa[miesiac])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
