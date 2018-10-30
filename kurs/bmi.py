#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py

def bmi(masa,wzrost):
    
    wzrost /= 100
    bmi = masa / (wzrost**2)
    
    print("BMI wynosi {:.1f}".format(bmi))
    
    if bmi < 18.5:
        print("Niedowaga!")
    elif bmi <= 24.9:
        print("Norma")
    elif bmi < 30:
        print("Nadwaga!")
    else:
        print("Otyłość!")
    
    
    

def main(args):
    
    masa = float(input("Podaj masę w kilogramach: "))
    wzrost = int(input("Podaj wzrost w centymetrach: "))
    
    bmi(masa,wzrost)
    
    """
    Pobierz masę w kilogramach
    pobierz wzrost w cm
    oblicz BMI wg wzoru: bmi = masa / (wzrost [m])^2
    wyprowadź wartość bmi oraz odpowiedni komunikat
        bmi < 18,5 - niedowaga
        18,5 - 24,9 - norma
        >= 25 nadwaga
        >= 30 otyłość
    """
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
