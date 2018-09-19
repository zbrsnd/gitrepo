#!/usr/bin/env python
# -*- coding: utf-8 -*-
def trojkat(a, b, c):
    """
    funkcja bada możliwość zbudowania trójkąta z trzech podanych boków
    funkcja zwraca true jezeli sie da, false w przeciwnym wypadku
    """
    
    if a + b > c and a + c > b and b + c > a:
        return True

    return False
    
    pass
    
    return
    

def main(args):
    
    a = int(input('Podaj 1. bok: '))
    b = int(input('Podaj 2. bok: '))
    c = int(input('Podaj 3. bok: '))
    
    if trojkat(a, b, c):
        print("Da się")
    else:
        print("Nie da się")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
