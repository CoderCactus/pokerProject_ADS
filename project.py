from random import randint

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []
        for i in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
            for j in ['clubs', 'hearts', 'diamonds', 'spades']:
                self.cards.append(Card(i, j))

    def shuffle(self):
        for i in range(len(self.cards)):
            randSeed = randint(i, len(self.cards)-1)
            self.cards[i], self.cards[randSeed] = swap(self.cards[i], self.cards[randSeed])
        
    def drawing(self, card_number):
        drawn = self.cards[:card_number]
        self.cards = self.cards[card_number:]
        
        return(drawn)
    
def swap(n, m):
    return m, n

deck = Deck()

deck.shuffle()

hand = deck.drawing(5)

for card in hand:
    print(card.value, card.suit)



