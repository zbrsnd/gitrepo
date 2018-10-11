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
        #    print(liczba) i j k 
        
            
def liczby3():
	
	licznik = 0
	for i in range(1,10): #cyfra setek
		for j in range(0,10): #cyfra dziesiatek
			for k in range(0,10): #cyfra jedności
				if (i != j and i != k) and (j != i and j != k) and (k != i and k != j):
					print("{}{}{} ".format(i,j,k), end='')
					licznik = licznik + 1         
	return licznik	

def main(args):
    print("\nLiczb 2-cyfrowych: ", liczby2())
    print("\nLiczb 3-cyfrowych: ", liczby3())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
