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
    def binarySort(self, cards=None):
        if cards is None:
            cards = self.cards
        for i in range(1, len(cards)):
            current = cards[i]
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                if current.numericValue < cards[mid].numericValue:
                    right = mid
                else:
                    left = mid + 1
            for j in range(i, left, -1):
                cards[j] = cards[j - 1]
            cards[left] = current
        return cards
    
    def mergeSort(self, cards=None):
        if cards is None:
            cards = self.cards

        if len(cards) <= 1:
            return cards

        mid = len(cards) // 2
        left = self.mergeSort(cards[:mid])
        right = self.mergeSort(cards[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].numericValue <= right[j].numericValue:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def otherSort():
        #TODO
        return
    
    def pokerDetection():
        #TODO
        return
    
def swap(n, m):
    return m, n

card_number = int(input('Insert the number of cards in the hand: '))

hand = Hand(card_number)

print(len(hand.cards))

for card in hand.cards:
    print(card.value, card.suit)

sorting_method = 0
if sorting_method == 1:
    hand.heapSort()
elif sorting_method == 2:
    hand.cards = hand.binarySort()
elif sorting_method == 3:
    hand.cards = hand.mergeSort()
elif sorting_method == 4:
    hand.cards = sorted(hand.cards , key=lambda x: x.numericValue)
    
for card in hand.cards:
        print(card.value, card.suit)

