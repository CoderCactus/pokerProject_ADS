from random import randint

class Card:
    def __init__(self, value, suit):
        """
        Adds two numbers together .
        Parameters :
            Value (str): The value of the card .
            Suit (str): The suit of the card ('♣', '♡', '♢' or '♠') .
        """
        self.value = value
        self.suit = suit

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
    
    def pokerDetection():
        #TODO #1
        return
    
def swap(n, m):
    return m, n

card_number = int(input('Insert the number of cards in the hand: '))

hand = Hand(card_number)

print(len(hand.cards))

for card in hand.cards:
    print(card.value, card.suit)



