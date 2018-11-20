#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
from datetime import date


class Samochod():
    """ Prosta klasa opisująca osobę """

    def __init__(self, marka, model, rokProdukcji, nadwozie):
        self.marka = model
        self.model = model
        self.rokProdukcji = rokProdukcji
        self.nadwozie = nadwozie

    def wiek(self):
        return date.today().year - self.rokProdukcji


auto = Samochod('Fiat', 'Tipo', 2005, 'sedan')
print(auto.wiek())
