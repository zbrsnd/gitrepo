#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
from peewee import * 

baza_plik = 'quiz.db'

################# MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza

class Kategoria(BazaModel):
    kategoria = CharField(null = False, unique = True)


class Pytanie(BazaModel):
    pytanie = CharField(null=False)
    kategoria = ForeignKeyField(Kategoria, related_name='pytania')


class Odpowiedz(BazaModel):
    odpowiedz = CharField(null=False)
    pytanie = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odp_ok = BooleanField(default=False)
