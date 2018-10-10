#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py


def liczby2():
    
    """
    Funkcja drukuje wszystkie liczby dwucyfrowe, 
    w których cyfry nie powtarzają się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 11, 22, 33 itd.
    """
    licznik = 0
    for i in range(1,10):
        for j in range(0,10):
            if i != j: 
                print("{}{} ".format(i,j), end='')
                licznik = licznik + 1
    return licznik


    #for liczba in range(10,100):
     #   if liczba % 10 == (liczba/10) % 10:
      #      print('',end='')
       # else:
        #    print(liczba)
        
            
            
    
    
    


def main(args):
    print("Liczb 2-cyfrowych: ", liczby2())
   # print("Liczb 3-cyfrowych: ", liczby3())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
