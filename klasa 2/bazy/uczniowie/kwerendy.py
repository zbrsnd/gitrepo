#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
import sqlite3

def kwerenda(cur):
    cur.execute(""" 
        
        WITH srednie AS(
        SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie   
        INNER JOIN oceny ON uczniowie.id  = oceny.id_uczen
        GROUP BY uczniowie.id)
        SELECT COUNT(nazwisko) FROM srednie
        WHERE sred > 3.5
        ORDER BY sred ASC
        
        

    """)
    
    #  WITH srednie AS(
    #  SELECT imie, nazwisko, AVG(ocena) AS sred FROM uczniowie   
    #  INNER JOIN oceny ON uczniowie.id  = oceny.id_uczen
    #  GROUP BY uczniowie.id)
    #  SELECT nazwisko, imie, sred FROM srednie
    #  WHERE sred > 3.5
    #  ORDER BY sred ASC 
    
    
    
    # AS <-- alias, nadaje inną  nazwę polu by móc ją później wykorzystać
            
    #  SELECT imie, nazwisko, klasa FROM uczniowie    
    #  INNER JOIN klasy ON uczniowie.id_klasa = klasy.id
    #  WHERE klasy.id = (SELECT klasy.id FROM klasy WHERE rok_naboru = 2012 AND klasa = '1A')
    
    # SELECT imie, nazwisko, klasa FROM uczniowie
    # INNER JOIN klasy ON uczniowie.id_klasa = klasy.id
    # WHERE rok_naboru = '2012' AND klasa = '1A'
    
    
    # SELECT MIN(egz_mat), AVG(egz_hum) itd.
    # SELECT MIN(kolumna) <- wybiera najmniejsza wartosc
    # SELECT MAX(kolumna) <- wybiera najwieksza wartosc
    # AVG(kolumna) <-- srednia arytmetyczna (AVERAGE)
    # LIMIT LICZBA
    # ORDER BY nazwisko ASC/DESC
    # WHERE plec = 1
    # % <-- dowolny ciąg znaków dowolnej długości
    # SELECT * FROM uczniowie WHERE nazwisko = 'A%'
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)
    




def main(args):
    
    # KONFIGURACJA #######
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda(cur)
    
    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
