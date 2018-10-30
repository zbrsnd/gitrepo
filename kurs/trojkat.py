#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
import math

def trojkat_bud(a,b,c):
    
    if a + b > c:
        if a + c > b:
            if b + c > a:
                trojkat = True
        
    if trojkat:
        print("Da się zbudować trójkąt")
        
    else:
        print("Nie da się zbudować trójkąta")
        
def heron(a,b,c):
    
    p = (a+b+c) / 2
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Pole: {:.4f}".format(pole))
    
def prost(a,b,c):
    trojkat_prost = False
    if a**2 + b**2 == c**2 or \
       a**2 + c**2 == b**2 or \
       b**2 + c**2 == a**2:
           trojkat_prost = True
        
    if trojkat_prost:
        print("Trójkąt prostokątny")
    else:
        print("Trójkąt nieprostokątny")
    
    

def main(args):
    
    a, b, c = eval(input("Podaj boki trójkąta, oddzielone przecinkami: ")) #eval --> evaluation, wykonaj, python traktuje tekst jako polecenie pythona
    print("Podano boki: {}. {}. {}".format(a,b,c) )
    
    trojkat = False
  
    
    trojkat_bud(a,b,c)
    heron(a,b,c)
    prost(a,b,c)
   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
