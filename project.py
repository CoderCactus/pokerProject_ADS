from random import randint # Imports function to generate random integers


class Card:
    def __init__(self, value, suit):
        """
        Adds two numbers together .
        Parameters :
            Value (str): The value of the card ('A','2','3','4','5','6','7','8','9','10','J','Q','K').
            Suit (str): The suit of the card ('♣', '♡', '♢' or '♠').

        """
        self.value = value # Original string value: '2','3','4','5','6','7','8','9','10','J','Q','K','A'
        self.suit = suit # Suit symbols: '♣', '♡', '♢' or '♠'

         # Assign a numeric value to non-numeric cards for sorting and comparison purposes
        if self.value == 'A':
            self.numericValue = 14
        elif self.value == 'J':
            self.numericValue = 11
        elif self.value == 'Q':
            self.numericValue = 12
        elif self.value == 'K':
            self.numericValue = 13
        else:
            self.numericValue = int(self.value) # Convert number cards to integers


class Deck:
    def __init__(self):
        '''
        Create a standard 52 card deck.
        Interates all values and suits to generate all possible combinations.
        '''
        self.cards = []
        for i in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            # for j in ['clubs', 'hearts', 'diamonds', 'spades']:
            for j in ['♣', '♡', '♢', '♠']:
                self.cards.append(Card(i, j)) #Add each card to the deck

    def shuffle(self):
        '''
        Shuffle the deck using Fisher-Yates algorithm.
        Randomly swaps cards from the deck between themselves.
        '''
        for i in range(len(self.cards)):
            randSeed = randint(i, len(self.cards) - 1) # Pick a random card index
            self.cards[i], self.cards[randSeed] = swap(self.cards[i], self.cards[randSeed]) # Swap the current card with the randomly chosen index card

    def drawing(self, card_number):
        '''
        Draws the input number(n) of cards from the deck.
        Removes drawn cards from the deck.
        '''
        drawn = self.cards[:card_number] # Take the n top cards of the deck
        self.cards = self.cards[card_number:] # Remove said n cards from the deck
        return (drawn)


class Hand:
    
    def __init__(self, card_number):
        '''
        Creates a hand by shuffling a new deck and drawing cards from it.
        '''
        deck = Deck() # Create a new standard deck of 52 cards (13 values × 4 suits)
        deck.shuffle() # Randomly shuffle the deck to ensure the cards are random
        self.cards = deck.drawing(card_number) # Draw n cards form the sfuffled deck into the hand

    def heapSort(self):
        '''
        Sorts cards in the hand using Heap Sort.
        Build heap and extract elements one by one.
        '''
        n = len(self.cards) # Gtes the number of cards of the hand
        for i in range(n // 2 - 1, -1, -1): 
            # Build max-heap starting from the last non-leaf node and heapify each node going upwards
            heapify(self.cards, n, i)
        for i in range(n - 1, 0, -1): 
            self.cards[0], self.cards[i] = self.cards[i], self.cards[0] # Swap the largest element(root) with the last element of the current heap
            heapify(self.cards, i, 0) # Heapify the reduced heap

    def binarySort(self):
        '''
        Sorts cards using Binary Insertion Sort.
        Finds the ordered position via binary search before inserting.
        '''
        for i in range(1, len(self.cards)): # Starts with the second card and interates through the rest of the hand.
            current = self.cards[i] # Defines the card to be inserted into the sorted position
            left, right = 0, i # Defines the initial bounds for the binary search
            while left < right:
                mid = (left + right) // 2 # Calculate the middle index of the current search range
                if current.numericValue < self.cards[mid].numericValue: 
                    # Checks if the card's numeric value is less than the middle card, it is placed before it
                    right = mid
                else:
                    # Otherwise, it goes afer the middle
                    left = mid + 1
            # Shift elements to the right to make space
            for j in range(i, left, -1):
                self.cards[j] = self.cards[j - 1]
            self.cards[left] = current # Insert the current card into its correct position


    def discard(self):
        '''
        Empties the current hand.
        '''
        self.cards = []


    def mergeSort(self, cards=None):
        '''
        Sorts the cards in the hand using Merge Sort.
        Splits the list and merges it again in sorted order.
        '''
        if cards is None:
            cards = self.cards
            # Guarantees that the cards on the hand are sorted if no other list is provided

        if len(cards) <= 1:
            return cards
        # Defines a hand with 0 or 1 cards as already softed

        mid = len(cards) // 2 # Finds the middle of the hand and divide it into two lists
        left = self.mergeSort(cards[:mid]) # Sorts the left half recursively
        right = self.mergeSort(cards[mid:]) # Sorts the left half recursively


        merged = self.merge(left, right) # Merge the tow halves creating one sorted list

        self.cards = merged # Update the hand's cards
        return merged

    def merge(self, left, right):
        '''
        Allows for Merge Sort to merge two lists
        '''
        result = [] # Creates an empty list to hold the merged result
        i = j = 0 # Initializes counters for left and right lists, respectively
        while i < len(left) and j < len(right):
            # Append the smaller element to the result and add one to the respective counter
            if left[i].numericValue <= right[j].numericValue:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:]) # Add remaining elements from the left list to the merged result list
        result.extend(right[j:]) # Add remaining elements from the right list to the merged result list
        return result

    def insertionSort(self):
        '''
        Sorts cards in the hand using the InsertionSort algorithm.
        '''
        for i in range(1, len(self.cards)): 
            current_card = self.cards[i] # Defines which card is to be placed in the correct position
            j = i - 1 # Defines j for comparison with the previous card purposes

            # Shift cards to the right if they are larger than the current one
            while j >= 0 and current_card.numericValue < self.cards[j].numericValue:
                self.cards[j + 1] = self.cards[j] # Shift card one position to the right
                j -= 1 # Move left in the list 

            # Insert the current card at the correctly sorted position
            self.cards[j + 1] = current_card

        return self.cards

    def pokerDetection(self):
        '''
        Detects and prints different poker hands from the current cards,
        and updates a hand tally with the count of each hand detected.
        '''
        # Detects all possible poker hands
        royalFlush = find_royalFlush(self.cards)
        straightFlush = find_straightFlush(self.cards)
        fourKind = find_fourKind(self.cards)
        fullHouse = find_fullHouse(self.cards)
        flush = find_flush(self.cards)
        straight = find_straight(self.cards)
        threeKind = find_threeKind(self.cards)
        twoPairs = find_twoPairs(self.cards)
        pair = find_pair(self.cards)

        # Check if any Royal Flushes were found (10-A of same suit).
        if len(royalFlush) != 0:
            hand_tally['royalFlush'] += len(royalFlush)
            for suit in royalFlush:
                print(f'Royal Straight of {suit[1]}')

        # Check if any Straight Flushes were found (5 consecutive cards of same suit).       
        if len(straightFlush) != 0:
            hand_tally['straightFlush'] += len(straightFlush)
            
            for val in straightFlush:
                print(f'Straight Flush of {val[0][0].value} to {val[0][-1].value} and suit {val[1][0]}')

        # Check if any Four of a Kind were found (4 cards of same rank).
        if len(fourKind) != 0:
            hand_tally['fourKind'] += len(fourKind)
            for val in fourKind:
                print(f'Four of a Kind of {val}')

        # Check if any Full Houses were found (3 cards of sama rank and 2 of other).
        if len(fullHouse) != 0:
            hand_tally['fullHouse'] += len(fullHouse)
            
            for val in fullHouse:
                print(f'Found a full house of {val[0]} and {val[1]}')

        # Check if any Flushes were found (5 cards of same suit).
        if len(flush) != 0:
            hand_tally['flush'] += len(flush)
                    
            for suit in flush:
                print(f'Flush of {suit}')

        # Check if any Straights were found (5 consecutive of different suit).
        if len(straight) != 0:
            hand_tally['straight'] += len(straight)

            for val in straight:
                print(f'Straight between {val[0].value} and {val[-1].value}')

        # Check if any Three of a Kind were found (3 of same rank).
        if len(threeKind) != 0:
            hand_tally['threeKind'] += len(threeKind)

            for val in threeKind:
                print(f'Three of a Kind of {val}')

        # Check if any Two Pairs were found (2 cards of a rank and 2 of another).
        if len(twoPairs) != 0:
            hand_tally['twoPairs'] += len(twoPairs)
            
            for val in twoPairs:
                    print(f'Two pairs of {val[0]} and {val[1]}')

        # Check if any Pairs were found (2 cards of the same rank).
        if len(pair) != 0:
            hand_tally['pair'] += len(pair)
            for i in pair:
                print(f'One Pair of {i}')
        
def find_pair(lst):
    i = 0 #Creates a counter for the number of pairs
    output = []  # Creates an empty list to store the values of found pairs
    while True:
        # Break the loop if index reaches the end of the list
        if i >= len(lst):
            break
        # Check if there is a following element and if it forms a pair with the current one
        elif i+1 < len(lst) and lst[i].value ==  lst[i+1].value:
            output.append(lst[i].value)
            i += 2 # Skip the next element as it's part of the current pair
        else:
            i += 1 # Move to the next element if no pair is found
    return output


def find_twoPairs(lst):
    output = [] # Creates an empty list to store the values of found two pairs
    first_pair = find_pair(lst) # Call find_pair function getting all the single pairs
    if len(first_pair) >= 2: # Check if there are two pairs of the same rank
        for i in range(0, len(first_pair), 2): # Iterate over the list of pair values, stepping by 2
            if i+1 < len(first_pair):  # Ensure we do not go out of bounds
                output.append([first_pair[i], first_pair[i+1]]) # Append both pairs to the output list
    return output


def find_threeKind(lst):
    output = [] # Creates an empty list to store the values of found three of a kind hands
    i = 0 #Creates a counter for the index
    while True:
        # Break the loop if index reaches the end of the list
        if i >= len(lst):
            break
         # Check if there are at least three cards remaining and if the current and following two cards have the same rank
        elif i+2 < len(lst) and lst[i].value ==  lst[i+1].value and  lst[i].value ==  lst[i+2].value:
            output.append(lst[i].value) # Add the value of the three-of-a-kind to the output list
            i += 3  # Skip the next two indices as they are part of the three of a kind
        else:
            i += 1 # Move to the next card if no match found
    return output


def find_straight(lst):
    output = []  # To store found straight hands

    # Remove duplicate numeric values, preserving order
    seen = set()
    ordered_unique = []
    for card in lst:
        if card.numericValue not in seen:
            ordered_unique.append((card.numericValue, card))
            seen.add(card.numericValue)

    # Handle Ace as low (1)
    extended = list(ordered_unique)
    for value, card in ordered_unique:
        if value == 14:  # Ace
            low_ace = Card('A', card.suit)
            low_ace.numericValue = 1
            extended.insert(0, (1, low_ace))
            break

    i = 0
    while i <= len(extended) - 5:
        values = [extended[i + j][0] for j in range(5)]
        if values == list(range(values[0], values[0] + 5)):
            needed = set(values)
            straight = []
            used_cards = []
            for card in lst:
                val = card.numericValue
                if val == 14 and 1 in needed:
                    val = 1
                if val in needed:
                    straight.append(card)
                    used_cards.append(card)
                    needed.remove(val)
                if not needed:
                    break
            if len(straight) == 5:
                output.append(straight)
                lst = [c for c in lst if c not in used_cards]  # Remove used cards
        i += 1

    return output


def find_flush(lst):
    output = [] # Creates an empty list to store the values of found flushes
    for i in ['♣', '♡', '♢', '♠']:
        count = 0 # Reset counter for each suit
        # Count how many cards in the list have the current suit
        for j in lst:
            if j.suit == i:
                count += 1
            # 5 cards of the same suit correspond to a flush
            if count == 5:
                output.append(i) # Add the suit to output list
    return output
        
def find_fullHouse(lst):
    output = [] # Creates an empty list to store the values of found full houses
    # Loop through each "three of a kind" found in the list
    for three in find_threeKind(lst):
        remaining_cards = [i for i in lst if i.value != three]  # Remove all cards of the same value as the three of a kind from the list so that they are not repeated in the pair
        for pair in find_pair(remaining_cards):  # Look for pairs in the remaining cards
            output.append([pair, three]) # Append a full house combination
            break

    return output

def find_fourKind(lst):
    output = [] # Creates an empty list to store the values of found four of a kind hands
    i = 0 #Creates a counter for the index
    while True:
        # Break loop if we've reached the end of the list
        if i >= len(lst):
            break
        # Check if there are at least 4 remaining cards and if the following 4 cards all have the same rank
        elif i+3 < len(lst) and lst[i].value ==  lst[i+3].value:
            output.append(lst[i].value) # Append the value to the output list as a four of a kind is found
            i += 4 # Skip past these four cards
        else:
            i += 1 # Move to the next card
    return output


def find_straightFlush(lst):
    output = [] # Creates an empty list to store the values of found straight flushes
    # Assumes cards are sorted and Ace is high (14)
    straights = find_straight(lst)
    
    for straight in straights:
        suits = [card.suit for card in straight] # Extract the suit of each card in the straight
        if all(s == suits[0] for s in suits):  # Check if cards are all same suit
            output.append((straight, suits[0])) # Append the value to the output list as a straight flush is found
    return output


def find_royalFlush(lst):
    output = [] # Creates an empty list to store the values of found royal flushes
    straightFlushes = find_straightFlush(lst)  # Get all straight flushes from the given list of cards

    for straight, suit in straightFlushes:
        values = [card.numericValue for card in straight] # Extract the numeric values of the cards in the straight flushes
        
        if sorted(values) == [10, 11, 12, 13, 14]: # Check if the straight is specifically a royal flush
            output.append((straight, suit)) # Append the value to the output list as a royal flush is found
    return output
    

def swap(n, m):
    '''
    Swaps two values
    '''
    return m, n


def heapify(array, n, i):
    '''
    Function to maintain the max-heap property for a subtree rooted at index i
    '''
    parent = i # Defines parent as root
    left = 2 * i + 1 # Left child index
    right = 2 * i + 2 # Right child index

    # If left child exists and is greater than the parent, update parent
    if left < n and array[left].numericValue > array[parent].numericValue:
        parent = left

    # If right child exists and is greater than the current parent, update parent
    if right < n and array[right].numericValue > array[parent].numericValue:
        parent = right

    # If the parent has changed, swap and recursively heapify the affected subtree
    if parent != i:
        array[i], array[parent] = array[parent], array[i] # Swap parent and current node
        heapify(array, n, parent) # Recursively heapify the affected subtree


hand_tally = {'pair': 0,
              'twoPairs': 0,
              'threeKind': 0,
              'straight': 0,
              'flush': 0,
              'fullHouse': 0,
              'fourKind': 0,
              'straightFlush': 0,
              'royalFlush': 0}

if __name__ == "__main__":
    while True:
        try:
            card_number_input = input('Insert the number of cards in the hand: ') # User input for the number of cards in the hand
            card_number = int(card_number_input)
            # Validate input range
            if card_number < 3:
                print('Please enter a number bigger than 3.')
                continue
            if card_number > 15:
                print('Please enter a number less or equal than 15.')
                continue

            hand = Hand(card_number) # Create a hand with the given number of cards

            # Display the unsorted cards
            for card in hand.cards:
                print(card.value, card.suit)
            # Ask user for sorting_method
            sorting_method_input = input('Select sorting method: (1- Heap Sort; 2- Binary Sort; 3- Merge Sort; 4- Insertion Sort): ')
            sorting_method = int(sorting_method_input)
            # Validate sorting method input
            if sorting_method not in [1, 2, 3, 4]:
                print('Invalid choice. Please select a number between 1 and 4.')
                continue

            # Sort the hand using the selected sorting algorithm
            if sorting_method == 1:
                hand.heapSort()
            elif sorting_method == 2:
                hand.binarySort()
            elif sorting_method == 3:
                hand.mergeSort()
            elif sorting_method == 4:
                hand.insertionSort()

            # Display the sorted cards
            for card in hand.cards:
                print(card.value, card.suit)
            
            # Detect and tally poker hands in the sorted cards
            hand.pokerDetection()

            # Print the tally of each combination found
            print('Combination Tally: ')
            for combination in hand_tally.keys():
                print(f'{combination}: {hand_tally[combination]}')

            # Ask the user if they want to continue playing
            if input('Do you want to continue? (yes/no): ').lower() != 'yes':
                print('Exiting the program. Goodbye!')
                break 
        # Handle non-integer inputs 
        except ValueError:
            print('Invalid input. Please enter a valid number.')