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
        royalFlush = find_royalFlush(self.cards)
        straightFlush = find_straightFlush(self.cards)
        fourKind = find_fourKind(self.cards)
        fullHouse = find_fullHouse(self.cards)
        flush = find_flush(self.cards)
        straight = find_straight(self.cards)
        threeKind = find_threeKind(self.cards)
        twoPairs = find_twoPairs(self.cards)
        pair = find_pair(self.cards)

        '''
        if royalFlush != False:
            #TODO

        if straightFlush != False:
            #TODO

        '''
        if fourKind != False:
            #TODO
            print(f'Four of a Kind of {fourKind}')

        if fullHouse != False:
            print(f'Found a full house of {fullHouse}')

        if flush != False:
            print(f'Flush of {flush}')

        if straight != False:
            print(f'Straight between {straight[0]} and {straight[1]}')

        if threeKind != False:
            print(f'Tree of a Kind of {threeKind}')

        if twoPairs != False:
            print(f'Two pairs of {twoPairs[0]} and {twoPairs[1]}')

        if pair != False:
            print(f'One Pair of {pair}')
        

def find_pair(lst):
    i = 0
    firstPair = -1
    while True:
        if i >= len(lst):
            break
        elif i+1 < len(lst) and lst[i].value ==  lst[i+1].value:
            #print(f'One Pair of {lst[i].value}')
            return lst[i].value
        else:
            i += 1
    return False

def find_twoPairs(lst):
    first_pair = find_pair(lst)
    if not first_pair:
        return False
    remaining_cards = [i for i in lst if i.value != first_pair]
    second_pair = find_pair(remaining_cards)
    if second_pair:
        return first_pair, second_pair
    else:
        return False

def find_threeKind(lst):
    i = 0
    while True:
        if i >= len(lst):
            break
        elif i+2 < len(lst) and lst[i].value ==  lst[i+1].value and  lst[i].value ==  lst[i+2].value:
            #print(f'Three of a Kind of {lst[i].value}')
            return lst[i].value
            i += 3
        else:
            i += 1
    return False

def find_straight(lst):
    for i in range(len(lst)-4):
        if lst[i].numericValue + 4 == lst[i+1].numericValue + 3 == lst[i+2].numericValue + 2  == lst[i+3].numericValue + 1 == lst[i+4].numericValue or (
          lst[i].numericValue + 3 == lst[i+1].numericValue + 2  == lst[i+2].numericValue + 1 == lst[i+3].numericValue and lst[i+4].value == 'A'  
        ) :
            return lst[i].value, lst[i+4].value
    return False

def find_flush(lst):
    for i in ['♣', '♡', '♢', '♠']:
        count = 0
        for j in lst:
            if j.suit == i:
                count += 1
            if count == 4:
                return i
    return False
        

def find_fullHouse(lst):
    pair = find_pair(lst)
    three = find_threeKind(lst)
    if find_pair(lst) and find_threeKind(lst):
        return pair, three
    else:
        return False

def find_fourKind(lst):
    i = 0
    while True:
        if i >= len(lst):
            break
        elif i+1 < len(lst) and lst[i].value ==  lst[i+3].value:
            return lst[i].value
        else:
            i += 4
    return False

def find_straightFlush(lst):
    return

def find_royalFlush(lst):
    return

            

def swap(n, m):
    return m, n

card_number = 5 #int(input('Insert the number of cards in the hand: '))

hand = Hand(card_number)
hand.cards = [Card('2', '♠'), Card('2', '♠'), Card('2', '♠'), Card('2', '♠'), Card('K', '♠')]

#print(len(hand.cards))

#Only for testing Purposes
#hand.cards = sorted(hand.cards , key=lambda x: x.numericValue)

for card in hand.cards:
   print(card.value, card.suit)

hand.pokerDetection()
