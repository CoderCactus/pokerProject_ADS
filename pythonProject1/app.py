import streamlit as st
import time
from pker_project import Hand, hand_tally

# --- Page Configuration ---
st.set_page_config(page_title="🃏 Poker Hand Analyzer", layout="centered")

st.title("🃏 Poker Hand Analyzer")
st.caption("Analyze poker hands using different sorting algorithms with stylish rendering.")

# --- Helper: Render Cards Nicely ---
def render_cards(cards):
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

# --- Sidebar Controls ---
st.sidebar.header("Settings")
card_number = st.sidebar.slider("Number of cards in hand", min_value=4, max_value=15, value=7)

sort_method = st.sidebar.selectbox(
    "Choose Sorting Method",
    options=["Heap Sort", "Binary Sort", "Merge Sort", "Insertion Sort"]
)

if st.sidebar.button("🃠 Deal Cards"):
    # --- Animated Shuffle Effect ---
    with st.spinner("Shuffling deck..."):
        progress = st.progress(0)
        for i in range(1, 101):
            time.sleep(0.01)  # Simulate shuffle time
            progress.progress(i)
        time.sleep(0.2)

    # Reset tally before new hand
    for key in hand_tally:
        hand_tally[key] = 0

    hand = Hand(card_number)

    st.subheader("🗂️ Cards Drawn")
    render_cards(hand.cards)

    # --- Sorting ---
    if sort_method == "Heap Sort":
        hand.heapSort()
    elif sort_method == "Binary Sort":
        hand.binarySort()
    elif sort_method == "Merge Sort":
        hand.mergeSort()
    elif sort_method == "Insertion Sort":
        hand.insertionSort()

    st.subheader("🔢 Sorted Cards")
    render_cards(hand.cards)

    # --- Poker Detection ---
    st.subheader("♠️ Poker Hand Detection")
    hand.pokerDetection()

    st.subheader("📊 Combination Tally")
    detected = False
    for key, value in hand_tally.items():
        if value > 0:
            st.success(f"**{key}**: {value}")
            detected = True

    if not detected:
        st.info("No poker combinations detected in this hand.")

