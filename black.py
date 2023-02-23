import os
import random


class Player:
    def __init__(self, score:int):
        self.score = score
        self.hand = {'S': [], 'D': [],'C': [], 'H':[]}
    
    def addScore(self, num:int):
        self.score += num
    
    def addHand(self, card:dict):
        for k, v in card.items():
            self.hand[k].append(v)

p1 = Player(0)
com = Player(0)


    
def draw(player:object, deck:dict):

    value_dict = {
        'k': 10,
        'Q': 10,
        'J': 10
        }
    
    deck = {
        'H':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        'D':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        'C':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        'S':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        }
    
    if player.score >= 10:
        value_dict.update({'A': 11})
    else:
        value_dict.update({'A': 1})
    
    rsuit = random.choice(list(deck.keys()))
    rvalue = random.choice(list(deck.get(rsuit)))
    
    if rvalue == str:
        newValue =  value_dict[rvalue]
        addToHand = {rsuit:newValue}
        for k, v in addToHand.items():
            player.addHandd[k] += v
    else:
        addToHand = {rsuit:rvalue}
        for k, v in addToHand.items():
            player.addHandd[k] += v        
    
        
    
    
    
    

        