#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#
# Obliczanie potęgi liczby naturalnej.


# ~def potega_it(a, n):
    
    # ~wynik = 1
    
    # ~for i in range(n):
        # ~wynik = wynik * a
        # ~#print(wynik)
        
    # ~return wynik   
    
    # ~pass
    
def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a
    
    
    
def main(args):
    
    #a = int(i nput("Podaj podstawę potęgi")
    #n = int(input("Podaj wykładnik potęgi")
    a, n = 2, 3
    print("Podstawa {} do potęgi {} wynosi {} ".
           format(a,n,potega_rek(a,n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
