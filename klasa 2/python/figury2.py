#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  Program drukuje wypełniony prostokąt o bokach podanych przez
#  użytkownika za pomocą podanego znaku


def prostokat1(a, b, znak):

    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()   
        
    return 0




def prostokat2(a, b, znak):
        
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b-1:
                print(znak, end='')
            else:
                print(" ", end='')
        print()   
        
    return 0
    
    
 #   return 0



def main(args):
    # pobieranie danych od użytkownika
    # boki prostokąta i znak
    a = int(input("Podaj długość 1 boku: "))
    b = int(input("Podaj długość 2 boku: "))
    znak = input("Podaj znak wypełnienia: ")
    
    prostokat1(a, b, znak)
    prostokat2(a, b, znak)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
