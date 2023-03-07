import random

class Player:
    def __init__(self, score:int, card:dict=None):
        self.score = score
        self.hand = {'S': [], 'D': [],'C': [], 'H':[]}
        self.card = card
    
    def addScore(self, num:int):
        self.score += num
        
    def scoreReset(self):
        self.score = 0
        self.hand = {'S': [], 'D': [],'C': [], 'H':[]}
    
    def addHand(self, card:dict):
        for k, v in card.items():
            self.hand[k].append(v)

class Deck:
    def __init__(self):

        self.startdeck = {
            'H':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
            'D':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
            'C':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
            'S':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
        } 
        
        self.value = {
            'K': 10,
            'Q': 10,
            'J': 10,
            '10':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,
            '4':4,
            '3':3,
            '2':2,
            'A':11
        }   
        
    def deckRefresh(self): 
        self.startdeck = {
            'H':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
            'D':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
            'C':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
            'S':['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
        } 

p1 = Player(0)
com = Player(0)
deck = Deck()

p1 = Player(0)
com = Player(0)

def gameReset():
 
    p1.scoreReset()
    com.scoreReset()
    deck.deckRefresh()


def winningConditions():
    conditions = {
        1: p1.score == 21 and com.score != 21,
        2: p1.score > 21,
        3: p1.score > com.score and p1.score <= 21,
        4: com.score == 21 and p1.score != 21,
        5: com.score > p1.score and com.score <= 21,
        6: com.score > 21,
        7: p1.score ==21 and com.score ==21 or p1.score == com.score, 
    }
    outcome = {
        1: f'Congratulations you won! with your score of {p1.score} BlackJack!',
        2: f'Sorry you busted with a score of {p1.score}',
        3: f'Congratulations you won! with your score of {p1.score} to the Dealers {com.score}',
        4: 'The Dealer has BlackJack',
        5: f'Sorry it looks like the Dealer has won with a score of {com.score} to your score of {p1.score}',
        6: f'The Dealer has busted with a score of {com.score}. Which makes you the winner.',
        7: "Looks like it's draw",
    }
    num = 1
    for k in conditions:
        if conditions[k] == True:
            print(outcome[num])
            print(com.hand)
            playAgain = input("Would you like to play again? (y/n)").lower()
            while True:
                if playAgain == 'y':
                    gameReset()
                    intialdraw()
                    playGame()
                elif playAgain == 'n':
                    exit()
                else:
                    print('Please choose valid option')
        else:
            num += 1
            continue
        
def intialdraw():
    runs = 2
    while runs != 0:
        rsuit = random.choice(list(deck.startdeck.keys()))
        rvalue = random.choice(list(deck.startdeck.get(rsuit)))
        
        newValue =  deck.value[rvalue]
        addToHand = {rsuit:rvalue}
        
        com.addHand(addToHand)
        com.addScore(newValue)
    
        deck.startdeck[rsuit].remove(rvalue)
    
        rsuit = random.choice(list(deck.startdeck.keys()))
        rvalue = random.choice(list(deck.startdeck.get(rsuit)))
        
        newValue =  deck.value[rvalue]
        addToHand = {rsuit:rvalue}
        
        p1.addHand(addToHand)
        p1.addScore(newValue)
        
        deck.startdeck[rsuit].remove(rvalue)
        runs -= 1
    
    if com.score == 21:
        print('Dealer drew 21, restart game.')
        gameReset()
        intialdraw()
    elif p1.score == 21:
        print('Great Job, you drew 21. Restarting game.')
        gameReset()
        intialdraw()
     
def draw(player:object):
    
    if player.score <= 10:
        deck.value.update({'A': 11})
    else:
        deck.value.update({'A': 1})
    
    rsuit = random.choice(list(deck.startdeck.keys()))
    rvalue = random.choice(list(deck.startdeck.get(rsuit)))
    
    newValue =  deck.value[rvalue]
    addToHand = {rsuit:rvalue}
    player.addHand(addToHand)
    player.addScore(newValue)
    
    deck.startdeck[rsuit].remove(rvalue)

def cpuLogic():
    while True:
        draw(com)
        if com.score > p1.score or (com.score >=17 and com.score == p1.score):
            winningConditions()
            
        else:
            continue
        
print("Welcome to Captlugnut's BlackJack")

def playGame():
    while True:
        if p1.score == 21:
            winningConditions()
        elif p1.score > 21:
            winningConditions()
        else:
            playMenu = str(input(f'''{p1.hand}
                  
                  Your Score: {p1.score}
                        
                    1. Hit
                    2. Stand
                                       
                    selection:'''))
            if playMenu == '1':
                draw(p1)
            elif playMenu == '2':
                cpuLogic()
            else:
                print("Please CHoose a valid option")
while True:
    selection = int(input('''
          1. Play a Game
          2. Exit
          Select: '''))
    if selection == 1:
        intialdraw()
        playGame()
    elif selection == 2:
        exit()
