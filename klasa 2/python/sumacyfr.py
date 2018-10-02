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







def main(args):

	suma = 0
	liczba = int(input("Podaj liczbę: "))
	while liczba != 0:
		suma += liczba % 10
		liczba /= 10

	print(int(suma)) 

  

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
