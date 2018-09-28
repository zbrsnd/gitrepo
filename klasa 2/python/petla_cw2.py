#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_cw2.py
#  
# DANE WEJSCIOWE:
# zmienne start i stop podane przez uzytkownika
# DANE WYJSCIOWE:   
# liczby naturalne z <start, stop> 
#print(i, "", end="")


def main(args):
    
    start = int(input('Podaj początek zakresu: '))
    stop = int(input('Podaj koniec zakresu: '))
    
    for i in range(start,stop+1):
        print(i, "", end="")
    
     
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
