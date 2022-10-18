import os
import random


class Player_Score:
    def __init__(self, tally):
        self.tally = tally

    def display(self):
        return self.tally

    def total(self, number: int):
        self.tally += number

    def score_to_zero(self, number: int):
        self.tally -= number

class Computer_Score:
    def __init__(self, ctally):
        self.ctally = ctally

    def computer_display(self):
        return self.ctally

    def ctotal(self, number: int):
        self.ctally += number

    def score_to_zero(self, number: int):
        self.ctally -= number

player_score = Player_Score(0)
computer_score = Computer_Score(0)
display_score = player_score.display()
computer_display_score = computer_score.computer_display()


def player_deck_update(hand: dict):

    rsuit = random.choice(list(deck.keys()))
    rvalue = random.choice(list(deck.get(rsuit)))

    if rvalue == 'J' or rvalue == 'K' or rvalue =='Q':
        player_score.total(10)
    elif rvalue == 'A':
        if player_score.display() >= 11:
            player_score.total(1)
        elif player_score.display() <= 10:
            player_score.total(11)
    else:
        player_score.total(rvalue)

    new_rvalue = str(rvalue)
        
    new_dict = {rsuit:rvalue}

    if rsuit not in hand:
        hand.update(new_dict)
    else:
        hand[rsuit] += [new_rvalue]
        
    deck[rsuit].remove(rvalue)

player_deck_update

def computer_deck_update(hand: dict):
    crsuit = random.choice(list(deck.keys()))
    crvalue = random.choice(list(deck.get(crsuit)))

    if crvalue == 'J' or crvalue == 'K' or crvalue =='Q':
        computer_score.ctotal(10)
    elif crvalue == 'A':
        if computer_score.computer_display() >= 11:
            computer_score.ctotal(1)
        elif computer_score.computer_display() <= 10:
            computer_score.ctotal(11)
    else:
        computer_score.ctotal(crvalue)

    new_rvalue = str(crvalue)
        
    new_dict = {crsuit:crvalue}

    if crsuit not in hand:
        hand.update(new_dict)
    else:
        hand[crsuit] += [new_rvalue]

computer_deck_update        
        
def draw(num: int, hand: dict):
    
    while True:
        if num == 0:
            break
        else:
            player_deck_update(hand)
            num -= 1

draw

def computer_draw(num: int, hand: dict):
    
    while True:
        if num == 0:
            break
        else:
            computer_deck_update(hand)
            num -= 1

computer_draw

deck = {
        'H':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        'D':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        'C':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
        'S':[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],
    }

player_hand= {
    'H': [], 
    'D': [],
    'C': [],
    'S': []
}

computer_hand= {
    'H': [], 
    'D': [],
    'C': [],
    'S': []
}

draw(1, player_hand)
computer_draw(1, computer_hand)
draw(1, player_hand)
computer_draw(1, computer_hand)

def reset_func():
    for k, v in player_hand.items():
        deck[k] += v
    for k, v in computer_hand.items():
        deck[k] += v
    for k, v in player_hand.items():
        player_hand[k] = []
    for k, v in player_hand.items():
        computer_hand[k] = []
    player_score.score_to_zero(player_score.display())
    computer_score.score_to_zero(computer_score.computer_display())
    draw(1, player_hand)
    computer_draw(1, computer_hand)
    draw(1, player_hand)
    computer_draw(1, computer_hand)
    os.system('cls')

def computer_logic(num:int):
    while True:
        print(computer_score.computer_display())
        if computer_score.computer_display() == 21:
            reset_selection = input(f'''
            Looks like the computer wins. Would you like to try again?

            Computer Score: {computer_score.computer_display()} vs Your Score: {num}
    
            1. Retry
            2. exit
    
            Your choice: 
            ''')
            if reset_selection == '1':
                reset_func()
            elif reset_selection == '2':
                quit()
            return reset_selection
        elif computer_score.computer_display() > num:
            reset_selection = input(f'''
            Looks like the computer wins. Would you like to try again?

            Computer Score: {computer_score.computer_display()} vs Your Score: {num}
    
            1. Retry
            2. exit
    
            Your choice: 
            ''')
            if reset_selection == '1':
                reset_func()
            elif reset_selection == '2':
                quit()
            return reset_selection
        elif computer_score.computer_display() > 21:
            reset_selection = input(f'''
            Looks like You win. Would you like to try again?

            Computer Score: {computer_score.computer_display()} vs Your Score: {num}
    
            1. Retry
            2. exit
    
            Your choice: 
            ''')
            if reset_selection == '1':
                reset_func()
            elif reset_selection == '2':
                quit()
            return reset_selection
        elif computer_score.computer_display() == num and computer_score.computer_display() < 17:
            computer_draw(1, computer_hand)
        elif computer_score.computer_display() == num:
            reset_selection = input(f'''
            Looks like its a TIE. Would you like to try again?

            Computer Score: {computer_score.computer_display()} vs Your Score: {num}
    
            1. Retry
            2. exit
    
            Your choice: 
            ''')
            if reset_selection == '1':
                reset_func()
            elif reset_selection == '2':
                quit()
            return reset_selection
        
        elif computer_score.computer_display() < num:
            computer_draw(1, computer_hand)
        
def main():
    while True:
        print(f"Your current score: {player_score.display()}")

        if player_score.display() == 21:
            repeat = input(
                '''
                Congrats, it appears you have won! Press 1 to play again or 2 to quit.
                ''')
            if repeat == '1':
                reset_func()
                continue
            elif repeat == '2':
                break
        elif player_score.display() > 21:
            repeat = input(
                '''
                Oh no! Looks like you went over 21.
                ''')
            if repeat == '1':
                reset_func()
                continue
            elif repeat == '2':
                break
            break
        
        player_hand_format="""
            Hearts : {H}
            Diamond: {D}
            Clubs  : {C}
            Spades : {S}
            """.format(**player_hand)
        print(player_hand_format)

        selection = input(
            '''
            1. Stand

            2. Hit

            What would you like to do?:  
            ''')

        if selection == '1':
            num = player_score.display()
            computer_logic(num)
            
        elif selection == '2':
            draw(1, player_hand)

main()