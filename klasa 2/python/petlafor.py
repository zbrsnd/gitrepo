#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    start = int(input('Podaj początek zakresu: '))
    stop = int(input('Podaj koniec zakresu: '))
    
    while start >= stop: #while - jeżeli warunek nie zostanie spełniony, pętla zacznie wykonywać się od początku [pętla nieskonćzona]
        
        start = int(input('Błędny zakres. Podaj inny: '))
        stop = int(input('Podaj koniec nowego zakresu: '))
        
    for liczba in range(start, stop+1): #stop+1 poniewaz koncowa liczba zakresu jest pomijana
        
        if liczba % 2 == 0: #jeśli liczba przy dzieleniu przez 2 daje 0 wydrukuj tę liczbę [tzn ze jest podzielna przez 2]
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
