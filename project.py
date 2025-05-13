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
    

    def insertionSort(self):
        for i in range(1, len(self.cards)):
            current_card = self.cards[i]
            j = i - 1
            
            # Shift larger cards to the right
            while j >= 0 and current_card.numericValue < self.cards[j].numericValue:
                self.cards[j + 1] = self.cards[j]
                j -= 1
            
            # Insert the current card at the correct position
            self.cards[j + 1] = current_card
        
        return self.cards
    
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

        
        if royalFlush != False:
            hand_tally['royalFlush'] += 1
            print(f'Royal Straight of {royalFlush}')
        
        if straightFlush != False:
            hand_tally['straightFlush'] += 1
            print(f'Straight Flush of {straightFlush[0][0].value} to {straightFlush[0][-1].value} and suit {straightFlush[1]}')

        if fourKind != False:
            hand_tally['fourKind'] += 1
            print(f'Four of a Kind of {fourKind}')

        if fullHouse != False:
            hand_tally['fullHouse'] += 1
            print(f'Found a full house of {fullHouse[0]} and {fullHouse[1]}')

        if flush != False:
            hand_tally['flush'] += 1
            print(f'Flush of {flush}')

        if straight != False:
            hand_tally['straight'] += 1
            print(f'Straight between {straight[0].value} and {straight[-1].value}')

        if threeKind != False:
            hand_tally['threeKind'] += 1
            print(f'Three of a Kind of {threeKind}')

        if twoPairs != False:
            hand_tally['twoPairs'] += 1
            print(f'Two pairs of {twoPairs[0]} and {twoPairs[1]}')

        if pair != False:
            hand_tally['pair'] += 1
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
            return lst[i:i+5]
    return False

def find_flush(lst):
    for i in ['♣', '♡', '♢', '♠']:
        count = 0
        for j in lst:
            if j.suit == i:
                count += 1
            if count == 5:
                return i
    return False
        
def find_fullHouse(lst):
    three = find_threeKind(lst)
    if not three:
        return False
    remaining_cards = [i for i in lst if i.value != three]
    pair = find_pair(remaining_cards)
    if pair:
        return pair, three
    
    return False

def find_fourKind(lst):
    i = 0
    while True:
        if i >= len(lst):
            break
        elif i+3 < len(lst) and lst[i].value ==  lst[i+3].value:
            return lst[i].value
        else:
            i += 4
    return False

def find_straightFlush(lst):
    straight = find_straight(lst)
    if not straight:
        return False
    
    flush = find_flush(straight)

    if flush != False:
        return straight, flush
    
    return False

def find_royalFlush(lst):
    straightFlush = find_straightFlush(lst)

    if not straightFlush:
        return False
    
    values = [i.value for i in straightFlush[0]]
    if values == ['10','J', 'Q', 'K', 'A'] :
        return straightFlush[1]
    
    return False

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


hand_tally = {'pair': 0, 
              'twoPairs': 0, 
              'threeKind': 0, 
              'straight': 0, 
              'flush': 0, 
              'fullHouse': 0, 
              'fourKind': 0, 
              'straightFlush': 0, 
              'royalFlush': 0}

#Only for testing Purposes

'''
card_number = 20 #int(input('Insert the number of cards in the hand: '))


hand = Hand(card_number)
#hand.cards = [Card('A', '♠'), Card('A', '♠'), Card('A', '♠'), Card('3', '♠'), Card('4', '♠')]

for card in hand.cards:
   print(card.value, card.suit)

hand.pokerDetection()
'''


while True:
    try:
        # Validate card_number
        card_number_input = input('Insert the number of cards in the hand: ')
        
        card_number = int(card_number_input)
        if card_number <= 0:
            print('Please enter a positive number.')
            continue
        if card_number > 52:
            print('Please enter a number less than or equal to 52.')
            continue

        # Validate sorting_method
        sorting_method_input = input('Select sorting method: (1- Heap Sort; 2- Binary Sort; 3- Merge Sort; 4- Other): ')
        sorting_method = int(sorting_method_input)
        if sorting_method not in [1, 2, 3, 4]:
            print('Invalid choice. Please select a number between 1 and 4.')
            continue

        # If both inputs are valid, proceed
        hand = Hand(card_number)

        if sorting_method == 1:
            hand.heapSort()
        elif sorting_method == 2:
            hand.binarySort()
        elif sorting_method == 3:
            hand.mergeSort()
        elif sorting_method == 4:
            #hand.cards = sorted(hand.cards, key=lambda x: x.numericValue) #ONLY FOR TESTING
            hand.insertionSort()
        
        for card in hand.cards:
            print(card.value, card.suit)

        hand.pokerDetection()
        
        print('Combination Tally: ')
        for combination in hand_tally.keys():
            print(f'{combination}: {hand_tally[combination]}') 
        
        if input('Do you want to continue? (yes/no): ').lower() != 'yes':
            print('Exiting the program. Goodbye!')
            break

    except ValueError:
        print('Invalid input. Please enter a valid number.')