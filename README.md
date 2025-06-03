# Poker Hand Evaluator and Card Sorter

This Python project simulates a deck of cards and allows creation of hands, sorting them using multiple algorithms, and evaluating for various poker combinations.

## Features

- Standard 52-card deck with suits: Clubs, Hearts, Diamonds, Spades and values: A, 2–10, J, Q, K  
- Shuffle using Fisher-Yates algorithm  
- Draw cards into a hand  
- Sorting Algorithms:
  - Heap Sort
  - Binary Insertion Sort
  - Merge Sort
  - Quick Sort  
- Poker Hand Detection:
  - Royal Flush
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pairs
  - Pair

## Project Structure

- `Card`: Represents an individual playing card  
- `Deck`: Creates and manages the 52-card deck  
- `Hand`: Draws, sorts, and evaluates a hand  
- Poker detection functions (e.g., `find_pair`, `find_flush`) identify various hand combinations


# Poker Hand Analyzer App

A Streamlit web app to draw poker hands, sort them using different algorithms, and detect classic poker combinations with stylish card rendering.

---

## Requirements

- Python 3.8 or higher

Install the required Python package:

```bash
pip install streamlit
````
---
# How to Run the App
Clone or download the project files to your local machine.

Ensure app.py and project.py are in the same folder.

Open a terminal or command prompt in that folder.

Run the Streamlit app:

```bash
streamlit run app.py
````
Your default browser will automatically open with the interface.
If it doesn’t, copy and paste the URL from the terminal (usually http://localhost:8501).

----
# Features
## Adjust Hand Size
   
Use the sidebar slider to select how many cards to draw (between 3 and 15).

## Choose a Sorting Method

Pick one of the following algorithms from the dropdown:

 - Heap Sort
  
 - Binary Sort
  
 - Merge Sort
  
 - Quick Sort

## Deal Cards
Click the "Deal Cards" button to:

- Shuffle the deck with animation

- Draw a random hand

- Display cards before and after sorting

- Detect poker combinations in real time

## View Detected Combinations
   
The app clearly displays any detected poker hands (e.g., Pair, Full House, Straight).

You’ll also see which specific cards make up each detected pattern.


