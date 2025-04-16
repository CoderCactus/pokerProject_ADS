from random import randint

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []
        for i in [1,2,3,4,5,6,7,8,9,10,'J','Q','K']:
            for j in ['clubs', 'hearts', 'diamonds', 'spades']:
                self.cards.append(Card(i, j))
        
    def drawing(self, card_number):
        drawn = []
    
        for i in range(card_number):
            randSeed = randint(i, len(self.cards))
            drawn.append(self.cards[randSeed])
            self.cards.pop(randSeed)
        
        return(drawn)

deck = Deck()

# Draw 5 cards
hand = deck.drawing(5)

# Print drawn cards
for card in hand:
    print(card.value, card.suit)



