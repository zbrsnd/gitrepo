#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pentle_cw_3.py
#  
# wyświetla kwadraty kolejnych liczb naturalnych, począwszy od zera a skończywszy na kwadracie liczby podanej przez użytkownika


def main(args):
	sqr = 0
	i = int(input("Podaj liczbę: "))
	
	for i in range(i+1):
		sqr = i*i
		print(sqr)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
