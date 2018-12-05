#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py

import turtle as t

def main():
    t.setup(800,600)
    t.color('blue', 'red')
    t.begin_fill()
    t.speed(0) 
    # ~figura(200,130,25)
    figura_rek(300,78,360,15)
    t.end_fill()
   
    
    return 0


# ~def figura(bok, kat, ile):
    # ~for i in range(ile):
        # ~t.forward(bok)
        # ~t.right(kat)
        
def figura_rek(bok, kat, ile, krok):
    t.forward(bok)
    t.right(kat)
    if ile > 0:
        figura_rek(bok-krok, kat, ile-1, krok)
    

main()
    
