#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


def kwerenda(cur):
    cur.execute("""
        WITH srednie AS (
            SELECT nazwisko, imie, AVG(ocena) AS sred FROM oceny
            INNER JOIN uczniowie ON uczniowie.id = oceny.id_uczen
            GROUP BY uczniowie.id
        ) SELECT COUNT(nazwisko) FROM srednie
        # w COUNT może być każde pole z srednie
        WHERE sred > 3.5
    """)
    """
    % --> dowolny ciąg znaków, dowolnej długości

    SELECT id FROM uczniowie WHERE imie='Anna' AND nazwisko='Ignaczuk'

    SELECT COUNT(*) FROM uczniowie WHERE imie LIKE '%a'

    SELECT COUNT(*) FROM uczniowie WHERE plec = 1

    SELECT imie, nazwisko, egz_mat FROM uczniowie
        WHERE egz_mat > 40 ORDER BY nazwisko ASC|DESC LIMIT 5

    SELECT AVG(egz_mat), AVG(egz_hum), AVG(egz_jez) FROM uczniowie

    SELECT MAX(egz_mat), MIN(egz_mat) FROM uczniowie

    SELECT imie, nazwisko, klasa FROM uczniowie
        INNER JOIN klasy ON uczniowie.id_klasa = klasy.id ORDER BY klasy ASC

    SELECT imie, nazwisko, klasa FROM uczniowie
        INNER JOIN klasy ON uczniowie.id_klasa = klasy.id
        WHERE klasy.id =
            (SELECT klasy.id FROM klasy
            WHERE klasa = '1A' AND rok_naboru = 2012)

    SELECT klasa, AVG(egz_mat) AS srM FROM klasy
        INNER JOIN uczniowie ON klasy.id = uczniowie.id_klasa
        GROUP BY klasy.id
        ORDER BY srM DESC

    WITH srednie AS (
            SELECT nazwisko, imie, AVG(ocena) AS sred FROM oceny
            INNER JOIN uczniowie ON uczniowie.id = oceny.id_uczen
            GROUP BY uczniowie.id)
    SELECT nazwisko, imie, sred FROM srednie
        WHERE sred > 3.5
        ORDER BY sred DESC LIMIT 10
    """
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)


def main(args):
    # KONFIGURACJA ####
    baza_nazwa = 'uczniowie'
    con = sqlite3.connect(baza_nazwa + '.db')
    cur = con.cursor()
    ###################
    kwerenda(cur)
    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
