#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
 

def main(args):
    suma = 0
    liczba = int(input("Podaj liczbę (minimum dwucyfrową): "))
    liczba = int(liczba)
    
    while liczba < 10:
        liczba = int(input("Błędne dane! Podaj inną liczbę: ")) 
        liczba = int(liczba)
        
    while liczba > 0:
            suma = int((suma + liczba % 10))
            liczba = int(liczba / 10)
            
        
    print(int(suma))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
