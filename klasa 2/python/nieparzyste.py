#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main(args):
    
    MAKS_liczba = 200 
    liczby = []
    licznik = 0
    
    #for i in range(200):
     #   liczba = random.randint(0, MAKS_liczba)
      #  id licz
    
    #program sumuje liczby nieparzyste spośród 200 wylosowanych liczb
    
    suma =0
    for i in range(200):        
        liczby.append(random.randint(0, MAKS_liczba)) #liczby append - dodawanie liczb do listy
    for liczba in liczby:
        if liczba % 2:
            licznik += 1
            suma = suma + liczba
            
    print(suma, licznik)
    
        

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
