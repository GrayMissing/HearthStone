import csv
import random
from cards import *

library = []
hand = []
battlefield = []
graveyard = []
exile = []
manapool = 0


class HearthStone:
    def __init__(self):
        global library
        cardfile = open('cards.csv', 'r')
        reader = csv.DictReader(cardfile)
        for row in reader:
            name = row['Name']
            cost = row['Cost']
            attack = row['Attack']
            health = row['Health']
            type = row['Type']
            minion = row['Minion/Spell']
            library.append(Card(name = name, cost = cost, attack = attack, health = health, type = type, minion = minion))
        random.shuffle(library)
    def round(self):            
        global library, hand, battlefield
        draw(library, hand)
        show(hand, battlefield)
def draw(library, hand):
    card = library.pop()
    hand.append(card)

def show(hand, battlefield, name = ''):
    for card in list(hand):
        battlefield.append(card)
        hand.remove(card)

if __name__ == '__main__':
    game = HearthStone()
    game.round()
    for card in battlefield:
        print card
