# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:23:09 2018

@author: orpha
"""

class Animal():
    def __init__(self, mass, genus, call):
        self.mass = mass
        self.genus = genus
        self.call = call
    def make_call(self):
        print(self.call)

wolf = Animal(5, 'canis', 'Hoooowwwwwllll!')
wolf.make_call()

class Pet(Animal):
    def __init__(self, mass, genus, call, human_friends):
        Animal.__init__(self, mass, genus, call)
        self.human_friends = human_friends

doggo = Pet(5, 'canis', 'Woof!', ['Em'])
doggo.make_call()
Pet.__dict__.get('human_friends')
doggo.__dict__.get('human_friends')
[key for key in doggo.__dict__.keys()]
doggo.make_call()
wolf.make_call()
dir(wolf)
