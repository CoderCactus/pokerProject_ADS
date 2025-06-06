import streamlit as st
import time
import project

# Page Configuration - Sets up the title and layout of the Streamlit app
st.set_page_config(page_title="Poker Hand Analyzer", layout="centered")

# Defines app title and subtitle
st.title("Poker Hand Analyser")

# Helper: Render Cards Nicely 
def render_cards(cards):
    '''
    Designs the list of card objects with HTML-styled visual blocks.
    Uses Unicode and color styling to represent card suits and values.
    '''
    suits_symbols = {'♠': '♠️', '♡': '♥️', '♢': '♦️', '♣': '♣️'}
    colors = {'♠': 'black', '♡': 'red', '♢': 'red', '♣': 'black'}

    styled = []
    for card in cards:
        color = colors[card.suit]
        suit = suits_symbols[card.suit]
        styled.append(
            f"<div style='display:inline-block; border:1px solid #ccc; padding:10px; margin:6px; "
            f"border-radius:12px; background:white; color:{color}; font-size:22px; text-align:center; "
            f"width:60px; height:90px; box-shadow:2px 2px 4px #aaa;'>{card.value}<br>{suit}</div>"
        )
    st.markdown("".join(styled), unsafe_allow_html=True)

# Sidebar Controls 
st.sidebar.header("Settings") # Adds user input controls in the sidebar
card_number = st.sidebar.slider("Number of cards in hand", min_value=3, max_value=15, value=7)

sort_method = st.sidebar.selectbox(
    "Choose Sorting Method",
    options=["Heap Sort", "Binary Sort", "Merge Sort", "Quick Sort"]
)

# Button to trigger dealing cards
if st.sidebar.button("Deal Cards"):
    # Animated Shuffle Effect 
    with st.spinner("Shuffling deck..."):
        progress = st.progress(0)
        for i in range(1, 101):
            time.sleep(0.01)  # Simulate shuffle time for visual effect
            progress.progress(i)
        time.sleep(0.2)

    # Reset hand tally before analyzing a new hand
    for key in project.hand_tally:
        project.hand_tally[key] = 0

    deck = project.Deck()
    # Generate new hand
    hand = project.Hand(card_number, deck)

    # Display drawn cards
    st.subheader("Cards Drawn")
    render_cards(hand.cards)

    # Sorting 
    # Sort the cards based on selected method
    if sort_method == "Heap Sort":
        hand.heapSort()
    elif sort_method == "Binary Sort":
        hand.binarySort()
    elif sort_method == "Merge Sort":
        hand.mergeSort()
    elif sort_method == "Quick Sort":
        hand.quickSort(0, len(hand.cards)-1)
    
    # Display sorted cards
    st.subheader("Sorted Cards")
    render_cards(hand.cards)

    # Poker Detection 
    # Analyze the hand for poker combinations
    st.subheader("Poker Hand Detection")

    # Detects all possible poker hands
    royalFlush = project.find_royalFlush(hand.cards)
    straightFlush = project.find_straightFlush(hand.cards)
    fourKind = project.find_fourKind(hand.cards)
    fullHouse = project.find_fullHouse(hand.cards)
    flush = project.find_flush(hand.cards)
    straight = project.find_straight(hand.cards)
    threeKind = project.find_threeKind(hand.cards)
    twoPairs = project.find_twoPairs(hand.cards)
    pair = project.find_pair(hand.cards)

    # Check if any Royal Flushes were found (10-A of same suit).
    if len(royalFlush) != 0:
        project.hand_tally['royalFlush'] += len(royalFlush)
        for suit in royalFlush:
            st.success(f'Royal Straight of {suit[1]}')

    # Check if any Straight Flushes were found (5 consecutive cards of same suit).       
    if len(straightFlush) != 0:
        project.hand_tally['straightFlush'] += len(straightFlush)
            
        for val in straightFlush:
            st.success(f'Straight Flush of {val[0][0].value} to {val[0][-1].value} and suit {val[1][0]}')

    # Check if any Four of a Kind were found (4 cards of same rank).
    if len(fourKind) != 0:
        project.hand_tally['fourKind'] += len(fourKind)
        for val in fourKind:
            st.success(f'Four of a Kind of {val}')

    # Check if any Full Houses were found (3 cards of same rank and 2 of other).
    if len(fullHouse) != 0:
        project.hand_tally['fullHouse'] += len(fullHouse)
            
        for val in fullHouse:
            st.success(f'Found a full house of {val[0]} and {val[1]}')

    # Check if any Flushes were found (5 cards of same suit).
    if len(flush) != 0:
        project.hand_tally['flush'] += len(flush)
                    
        for suit in flush:
            st.success(f'Flush of {suit}')

    # Check if any Straights were found (5 consecutive cards of different or same suit).
    if len(straight) != 0:
        project.hand_tally['straight'] += len(straight)

        for val in straight:
            st.success(f'Straight between {val[0].value} and {val[-1].value}')

    # Check if any Three of a Kind were found (3 of same rank).
    if len(threeKind) != 0:
        project.hand_tally['threeKind'] += len(threeKind)

        for val in threeKind:
            st.success(f'Three of a Kind of {val}')

    # Check if any Two Pairs were found (2 cards of a rank and 2 of another).
    if len(twoPairs) != 0:
        project.hand_tally['twoPairs'] += len(twoPairs)
            
        for val in twoPairs:
            st.success(f'Two pairs of {val[0]} and {val[1]}')

    # Check if any Pairs were found (2 cards of the same rank).
    if len(pair) != 0:
        project.hand_tally['pair'] += len(pair)
        for i in pair:
            st.success(f'One Pair of {i}')

    # Display combination results
    st.subheader("Combination Tally")
    detected = False
    for key, value in project.hand_tally.items():
        if value > 0:
            st.success(f"**{key}**: {value}")
            detected = True

    # If no combinations were detected
    if not detected:
        st.info("No poker combinations detected in this hand.")

    # Discards the current hand and resets the GUI
    if st.sidebar.button("Discard"):
        hand.discard()
