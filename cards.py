# from cardactions import *
from hearthstone import *
class Card:
    def __init__(self, name = '', text = '', cost = 0, attack = 0, health = 0, type = 'basic', minion = 'minion'):
        self.name = name
        self.text = text
        self.cost = cost
        self.attack = attack
        self.health = health
        self.type = type
        self.minion = minion
        self.buff = [0, 0]
        self.damaged = 0
    def __str__(self):
        return self.name
    def getname(self):
        return self.name        
    def getattack(self):
        return self.attack + self.buff[0]
    def gethealth(self):
        return self.health + self.buff[1] + self.damaged
    def getcost(self):
        return self.cost
    def buff(self, attack, health):
        self.buff[0] += attack
        self.buff[1] += health
    def damage(self, energe):
        if self.gethealth() > energe:
            self.damaged -= energe
    def heal(self, energe):
        if self.gethealth() + energe > self.health + self.buff[1]:
            self.damaged += energe
    def action(self):
        actionsdict[self.name]()
