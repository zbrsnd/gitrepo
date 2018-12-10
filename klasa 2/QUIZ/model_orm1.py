#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import os
from peewee import * 

baza_plik = 'quiz.db'

################# MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza


class Pytanie(BazaModel):
    pytanie = CharField(null=False, unique=True)
    odpok = ForeignKeyField
    
class Odpowiedz(BazaModel):
    pnr = ForeignKeyField(Pytanie, related_name ='odpowiedzi')
    odpowiedz = CharField(null=False)
    

