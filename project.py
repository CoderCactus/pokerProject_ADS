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
        
    def heapSort(self):
        n = len(self.cards)
        for i in range(n//2 - 1, -1, -1):
            heapify(self.cards, n, i)
        for i in range(n-1, 0, -1):
            self.cards[0], self.cards[i] = self.cards[i], self.cards[0]  
            heapify(self.cards, i, 0)
     
    def binarySort():
        #TODO
        return
    def mergeSort():
        #TODO
        return
    def otherSort():
        #TODO
        return
    
    def pokerDetection():
        #TODO
        return
    
def swap(n, m):
    return m, n


def heapify(array, n, i):
    parent = i
    left = 2*i+1
    right = 2*i+2

    if left < n and array[left].numericValue > array[parent].numericValue:
        parent = left

    if right < n and array[right].numericValue > array[parent].numericValue:
        parent = right

    if parent != i:
        array[i], array[parent] = array[parent], array[i]
        heapify(array, n, parent)


card_number = int(input('Insert the number of cards in the hand: '))

hand = Hand(card_number)

for card in hand.cards:
    print(card.value, card.suit)
print("potato")
#print(len(hand.cards))
hand.heapSort()
for card in hand.cards:
    print(card.value, card.suit)



