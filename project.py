from random import randint

class Card:
    def __init__(self, value, suit):
        """
        Adds two numbers together .
        Parameters :
            Value (str): The value of the card ('A','2','3','4','5','6','7','8','9','10','J','Q','K').
            Suit (str): The suit of the card ('♣', '♡', '♢' or '♠').

        """
        self.value = value
        self.suit = suit

        if self.value == 'A':
            self.numericValue = 1
        elif self.value == 'J':
            self.numericValue = 11
        elif self.value == 'Q':
            self.numericValue = 12
        elif self.value == 'K':
            self.numericValue = 13
        else:
            self.numericValue = int(self.value)

class Deck:
    def __init__(self):
        self.cards = []
        for i in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            #for j in ['clubs', 'hearts', 'diamonds', 'spades']:
            for j in ['♣', '♡', '♢', '♠']:
                self.cards.append(Card(i, j))

    def shuffle(self):
        for i in range(len(self.cards)):
            randSeed = randint(i, len(self.cards)-1)
            self.cards[i], self.cards[randSeed] = swap(self.cards[i], self.cards[randSeed])
        
    def drawing(self, card_number):
        drawn = self.cards[:card_number]
        self.cards = self.cards[card_number:]
        
        return(drawn)

class Hand:
    def __init__(self, card_number):
        deck = Deck()
        deck.shuffle()
        self.cards = deck.drawing(card_number)

    def discard(self):
        self.cards = []

    def heapSort():
        #TODO
        return 
    def binarySort():
        #TODO
        return
    def mergeSort():
        #TODO
        return
    def otherSort():
        #TODO
        return
    
    def pokerDetection(self):
        #TODO
        find_pair(self.cards)
        find_threes(self.cards)
        find_straight(self.cards)

        return

def find_pair(lst):
    i = 0
    firstPair = -1
    while True:
        if i >= len(lst):
            break
        elif i+1 < len(lst) and lst[i].value ==  lst[i+1].value:
            print(f'One Pair of {lst[i].value}')
            if firstPair != -1 and lst[firstPair].value != lst[i].value:
                print(f'Two Pairs of {lst[firstPair].value} and {lst[i].value}')
                firstPair = -1
            firstPair = i
            i += 2
        else:
            i += 1

def find_threes(lst):
    i = 0
    while True:
        if i >= len(lst):
            break
        elif i+2 < len(lst) and lst[i].value ==  lst[i+1].value and  lst[i].value ==  lst[i+2].value:
            print(f'Three of a Kind of {lst[i].value}')
            i += 3
        else:
            i += 1

def find_straight(lst):
    for i in range(len(lst)-4):
        if lst[i].numericValue + 4 == lst[i+1].numericValue + 3 == lst[i+2].numericValue + 2  == lst[i+3].numericValue + 1 == lst[i+4].numericValue:
            print(f'Straight between {lst[i].value} and {lst[i+4].value}')
            

def swap(n, m):
    return m, n

card_number = 4 #int(input('Insert the number of cards in the hand: '))

hand = Hand(card_number)
hand.cards = [Card('A', 'spades'), Card('2', 'clubs'), Card('3', 'spades'), Card('4', 'diamonds'), Card('5', 'hearts')]

#print(len(hand.cards))

for card in hand.cards:
   print(card.value, card.suit)

hand.pokerDetection()