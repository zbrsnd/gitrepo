#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person():
    """ Prosta klasa opisująca osoby"""
    def __init__(self, name, surname, healthPoint):
        self.name = name
        self.surname = surname
        self.setSex(name)
        self.healthPoint = healthPoint

    def setSex(self, imie):
        if imie[- 1] == 'a':
            self.sex = 'female'
            self.attack = 3
            self.defendce = 1
        else:
            self.sex = 'male'
            self.attack = 5
            self.defendce = 2

    def fight(self, person):
        person.defend(self.attack)

    def defend(self, attack):
        self.healthPoint -= (attack - self.defendce)
        if self.healthPoint < 1:
            print("I am dead")
        else:
            print("I am still allive! Hit one more time baby!")


karolina = Person('Karolina', 'Gwizd', 10)
print(karolina.surname, karolina.sex, karolina.healthPoint)

michal = Person('Michał', 'Świst', 10)
print(michal.surname, michal.sex, michal.healthPoint)


karolina.fight(michal)
michal.fight(karolina)
michal.fight(karolina)

print(karolina.healthPoint, michal.healthPoint)
