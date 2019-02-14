#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

kod = {
    'a' : '+-', 
    'b' : '-+++', 'c' : '-+-+', 'd' : '-++', 'e' : '+', 'f' : '++-+', 'g' : '--+', 'h' : '++++', 'i' : '++', 'j' : '+---', 'k' : '-+-', 'l' : '+-++', 'm' : '--', 'n' : '-+', 'o' : '---', 'p' : '+--+', 'q' : '--+-', 'r' : '+-+', 's' : '+++', 't' : '-', 'u' : '++-', 'v' : '+++-', 'w' : '+--', 'x' : '-++-', 'y' : '-+--', 'z' : '--++', 'ą' : '+-+-', 'ć' : '-+-++', 'ę' : '++-++', 'ch' : '----', 'ł' : '+-++-', 'ń' : '--+--', 'ó' : '---+', 'ś' : '+++-+++', 'ż' : '--++-+', 'ź': '--++-', ' ': ' ' }


def koduj(tekst):
    tekst = input('Podaj tekst: ')
    for l in tekst:
        print(kod[l])
    # tekst = input('Podaj tekst: ').lower()
    # print("".join(kod[l] for l in tekst))
    
def dekoduj():
    tekst = []
    lit = ' '
    while lit > '':
        lit = input("Podaj kod Morsea: ")
        tekst.append(lit)
    print(lit)


def main(args):
    # ~koduj(args)
    dekoduj()
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
