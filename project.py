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
            self.numericValue = 14
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
        for i in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            # for j in ['clubs', 'hearts', 'diamonds', 'spades']:
            for j in ['♣', '♡', '♢', '♠']:
                self.cards.append(Card(i, j))

    def shuffle(self):
        for i in range(len(self.cards)):
            randSeed = randint(i, len(self.cards) - 1)
            self.cards[i], self.cards[randSeed] = swap(self.cards[i], self.cards[randSeed])

    def drawing(self, card_number):
        drawn = self.cards[:card_number]
        self.cards = self.cards[card_number:]

        return (drawn)


class Hand:
    def __init__(self, card_number):
        deck = Deck()
        deck.shuffle()
        self.cards = deck.drawing(card_number)

    def heapSort(self):
        n = len(self.cards)
        for i in range(n // 2 - 1, -1, -1):
            heapify(self.cards, n, i)
        for i in range(n - 1, 0, -1):
            self.cards[0], self.cards[i] = self.cards[i], self.cards[0]
            heapify(self.cards, i, 0)

    def binarySort(self):
        for i in range(1, len(self.cards)):
            current = self.cards[i]
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                if current.numericValue < self.cards[mid].numericValue:
                    right = mid
                else:
                    left = mid + 1
            for j in range(i, left, -1):
                self.cards[j] = self.cards[j - 1]
            self.cards[left] = current


    def discard(self):
        self.cards = []


    def mergeSort(self, cards=None):
        if cards is None:
            cards = self.cards

        if len(cards) <= 1:
            return cards

        mid = len(cards) // 2
        left = self.mergeSort(cards[:mid])
        right = self.mergeSort(cards[mid:])


        merged = self.merge(left, right)

        self.cards = merged
        return merged

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

        royalFlush = find_royalFlush(self.cards)
        straightFlush = find_straightFlush(self.cards)
        fourKind = find_fourKind(self.cards)
        fullHouse = find_fullHouse(self.cards)
        flush = find_flush(self.cards)
        straight = find_straight(self.cards)
        threeKind = find_threeKind(self.cards)
        twoPairs = find_twoPairs(self.cards)
        pair = find_pair(self.cards)

        
        if len(royalFlush) != 0:
            hand_tally['royalFlush'] += len(royalFlush)
            for suit in royalFlush:
                print(f'Royal Straight of {suit[1]}')
        
        if len(straightFlush) != 0:
            hand_tally['straightFlush'] += len(straightFlush)
            
            for val in straightFlush:
                print(f'Straight Flush of {val[0][0].value} to {val[0][-1].value} and suit {val[1][0]}')

        if len(fourKind) != 0:
            hand_tally['fourKind'] += len(fourKind)
            for val in fourKind:
                print(f'Four of a Kind of {val}')

        if len(fullHouse) != 0:
            hand_tally['fullHouse'] += len(fullHouse)
            
            for val in fullHouse:
                print(f'Found a full house of {val[0]} and {val[1]}')


        if len(flush) != 0:
            hand_tally['flush'] += len(flush)
            
            for suit in flush:
                print(f'Flush of {suit}')

        if len(straight) != 0:
            hand_tally['straight'] += len(straight)

            for val in straight:
                print(f'Straight between {val[0].value} and {val[-1].value}')

        if len(threeKind) != 0:
            hand_tally['threeKind'] += len(threeKind)

            for val in threeKind:
                print(f'Three of a Kind of {val}')

        if len(twoPairs) != 0:
            hand_tally['twoPairs'] += len(twoPairs)
            
            for val in twoPairs:
                    print(f'Two pairs of {val[0]} and {val[1]}')

        if len(pair) != 0:
            hand_tally['pair'] += len(pair)
            for i in pair:
                print(f'One Pair of {i}')
        
def find_pair(lst):
    i = 0
    output = []
    while True:
        if i >= len(lst):
            break

        elif i+1 < len(lst) and lst[i].value ==  lst[i+1].value:
            #print(f'One Pair of {lst[i].value}')
            output.append(lst[i].value)
            i += 2

        else:
            i += 1
    return output


def find_twoPairs(lst):
    output = []
    first_pair = find_pair(lst)
    if len(first_pair) >= 2:
        for i in range(0, len(first_pair), 2):
            if i+1 < len(first_pair):
                output.append([first_pair[i], first_pair[i+1]])
    return output


def find_threeKind(lst):
    output = []
    i = 0
    while True:
        if i >= len(lst):
            break

        elif i+2 < len(lst) and lst[i].value ==  lst[i+1].value and  lst[i].value ==  lst[i+2].value:
            #print(f'Three of a Kind of {lst[i].value}')
            output.append(lst[i].value)


            i += 3
        else:
            i += 1
    return output


def find_straight(lst):

    output = []

    # Create a list of tuples (numericValue, card), maintaining order and uniqueness
    seen = set()
    ordered_unique = []
    for card in lst:
        if card.numericValue not in seen:
            ordered_unique.append((card.numericValue, card))
            seen.add(card.numericValue)

    # If Ace is present, simulate Ace as 1 at the beginning
    extended = list(ordered_unique)
    for value, card in ordered_unique:
        if value == 14:  # Ace
            low_ace = Card('A', card.suit)
            low_ace.numericValue = 1
            extended.insert(0, (1, low_ace))
            break

    # Detect 5 consecutive values
    for i in range(len(extended) - 4):
        values = [extended[i + j][0] for j in range(5)]
        if values == list(range(values[0], values[0] + 5)):
            needed = set(values)
            straight = []
            for card in lst:
                val = card.numericValue
                if val == 14 and 1 in needed:
                    val = 1
                if val in needed:
                    straight.append(card)
                    needed.remove(val)
                if not needed:
                    break
            output.append(straight)

    return output



def find_flush(lst):
    output = []
    for i in ['♣', '♡', '♢', '♠']:
        count = 0
        for j in lst:
            if j.suit == i:
                count += 1
            if count == 5:

                output.append(i)
    return output
        
def find_fullHouse(lst):
    output = []
    
    for three in find_threeKind(lst):
        remaining_cards = [i for i in lst if i.value != three]

        for pair in find_pair(remaining_cards):
            output.append([pair, three])
    
    return output

def find_fourKind(lst):
    output = []
    i = 0
    while True:
        if i >= len(lst):
            break

        elif i+3 < len(lst) and lst[i].value ==  lst[i+3].value:
            output.append(lst[i].value)
            i += 4
            
        else:
            i += 1
    return output


def find_straightFlush(lst):

    output = []

    # Assumes cards are sorted and Ace is high
    straights = find_straight(lst)
    
    for straight in straights:
        suits = [card.suit for card in straight]
        if all(s == suits[0] for s in suits):  # All same suit
            output.append((straight, suits[0]))
    
    return output



def find_royalFlush(lst):


    output = []
    straightFlushes = find_straightFlush(lst)

    for straight, suit in straightFlushes:
        values = [card.numericValue for card in straight]
        if sorted(values) == [10, 11, 12, 13, 14]:
            output.append((straight, suit))
    
    return output



def swap(n, m):
    return m, n


def heapify(array, n, i):
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2

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

# Only for testing Purposes

'''
card_number = 20 #int(input('Insert the number of cards in the hand: '))


hand = Hand(card_number)
#hand.cards = [Card('A', '♠'), Card('A', '♠'), Card('A', '♠'), Card('3', '♠'), Card('4', '♠')]

for card in hand.cards:
   print(card.value, card.suit)

hand.pokerDetection()
'''

if __name__ == "__main__":
    while True:
        try:
            card_number_input = input('Insert the number of cards in the hand: ')

            card_number = int(card_number_input)
            if card_number <= 3:
                print('Please enter a number bigger than 3.')
                continue
            if card_number > 15:
                print('Please enter a number less or equal than 15.')
                continue

            hand = Hand(card_number)

            for card in hand.cards:
                print(card.value, card.suit)
            # Validate sorting_method
            sorting_method_input = input(
                'Select sorting method: (1- Heap Sort; 2- Binary Sort; 3- Merge Sort; 4- Insertion Sort): ')
            sorting_method = int(sorting_method_input)
            if sorting_method not in [1, 2, 3, 4]:
                print('Invalid choice. Please select a number between 1 and 4.')
                continue

            # If both inputs are valid, proceed

            if sorting_method == 1:
                hand.heapSort()
            elif sorting_method == 2:
                hand.binarySort()
            elif sorting_method == 3:
                hand.mergeSort()
            elif sorting_method == 4:
                # hand.cards = sorted(hand.cards, key=lambda x: x.numericValue) #ONLY FOR TESTING
                hand.insertionSort()

            for card in hand.cards:
                print(card.value, card.suit)
            # Reset the tally before each hand

            hand.pokerDetection()

            print('Combination Tally: ')
            for combination in hand_tally.keys():
                print(f'{combination}: {hand_tally[combination]}')

            if input('Do you want to continue? (yes/no): ').lower() != 'yes':
                print('Exiting the program. Goodbye!')
                break

        except ValueError:
            print('Invalid input. Please enter a valid number.')

