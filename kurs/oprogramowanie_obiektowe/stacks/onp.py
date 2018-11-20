#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  onp.py

from stos_obj import Stos

def czy_poprawne(onp):
    for z in onp:
        if z.isalpha():
            return False
    return True

def main(args):
    stos = Stos()
    onp = input("Podaj wyr. ONP, oddzielające operandy i operatory spacjami:\n")
    # 3 3 7 + * = (3 + 7) * 3
    onp = onp.split(" ")
    if not czy_poprawne(onp):
        print("Błąd wyrażenia")
        return 0
    for el in onp:
        if el.isdigit():
            stos.push(el)
        else:
            a = stos.pop()
            b = stos.pop()
            stos.push(str(eval(b + el + a)))
    print("Wynik: ", stos.pop())
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
