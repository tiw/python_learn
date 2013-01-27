# -*- coding: utf-8 -*-


class Person:
    name = 'Adam'

    def getName(self):
        print self.name


def setName(self, name):
    self.name = name

Person.setName = setName

person = Person()

person.getName()

person.setName('Ting')

person.getName()


def sayChineseName(self):
    print '和你在一起'

Person.sayC = sayChineseName


person.sayC()


print type('和你在一起')