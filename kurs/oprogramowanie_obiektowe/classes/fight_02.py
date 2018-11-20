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
            self.__sex = 'female'
            self.__attack = 3
            self.__defendce = 1
        else:
            self.__sex = 'male'
            self.__attack = 5
            self.__defendce = 2

    def fight(self, person):
        person.defend(self.__attack)

    def defend(self, attack):
        self.healthPoint -= (attack - self.__defendce)
        if self.healthPoint < 1:
            print("I am dead")
        else:
            print("I am still allive! Hit one more time baby!")


karolina = Person('Karolina', 'Gwizd', 10)
print(karolina.__dict__)
# print(karolina.surname, karolina.sex, karolina.healthPoint)
exit()
michal = Person('Michał', 'Świst', 10)
# print(michal.surname, michal.sex, michal.healthPoint)


karolina.fight(michal)
michal.fight(karolina)


print(karolina.healthPoint, michal.healthPoint)
