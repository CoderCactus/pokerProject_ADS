import streamlit as st
import time
from project import Hand, hand_tally

# Page Configuration - Sets up the title and layout of the Streamlit app
st.set_page_config(page_title="🃏 Poker Hand Analyzer", layout="centered")

# Defines app title and subtitle
st.title("🃏 Poker Hand Analyzer")
st.caption("Analyze poker hands using different sorting algorithms with stylish rendering.")

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
            f"width:50px; height:70px; box-shadow:2px 2px 4px #aaa;'>{card.value}<br>{suit}</div>"
        )
    st.markdown("".join(styled), unsafe_allow_html=True)

# Sidebar Controls 
st.sidebar.header("Settings") # Adds user input controls in the sidebar
card_number = st.sidebar.slider("Number of cards in hand", min_value=4, max_value=15, value=7)

sort_method = st.sidebar.selectbox(
    "Choose Sorting Method",
    options=["Heap Sort", "Binary Sort", "Merge Sort", "Insertion Sort"]
)

# Button to trigger dealing cards
if st.sidebar.button("🃠 Deal Cards"):
    # Animated Shuffle Effect 
    with st.spinner("Shuffling deck..."):
        progress = st.progress(0)
        for i in range(1, 101):
            time.sleep(0.01)  # Simulate shuffle time for visual effect
            progress.progress(i)
        time.sleep(0.2)

    # Reset hand tally before analyzing a new hand
    for key in hand_tally:
        hand_tally[key] = 0

    # Generate new hand
    hand = Hand(card_number)

    # Display drawn cards
    st.subheader("🗂️ Cards Drawn")
    render_cards(hand.cards)

    # Sorting 
    # Sort the cards based on selected method
    if sort_method == "Heap Sort":
        hand.heapSort()
    elif sort_method == "Binary Sort":
        hand.binarySort()
    elif sort_method == "Merge Sort":
        hand.mergeSort()
    elif sort_method == "Insertion Sort":
        hand.insertionSort()

    # Display sorted cards
    st.subheader("🔢 Sorted Cards")
    render_cards(hand.cards)

    # Poker Detection 
    # Analyze the hand for poker combinations
    st.subheader("♠️ Poker Hand Detection")
    hand.pokerDetection()

    # Display combination results
    st.subheader("📊 Combination Tally")
    detected = False
    for key, value in hand_tally.items():
        if value > 0:
            st.success(f"**{key}**: {value}")
            detected = True

     # If no combinations were detected
    if not detected:
        st.info("No poker combinations detected in this hand.")