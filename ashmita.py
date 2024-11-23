import streamlit as st
import random

if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("Number Guessing Game")

st.write("""
    I have selected a number between 1 and 100. Try to guess it! 
    You can enter your guess below.
""")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button('Submit Guess'):
    st.session_state.attempts += 1
    
    if guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
        st.session_state.number_to_guess = random.randint(1, 100)  # Reset the number for a new game
        st.session_state.attempts = 0  # Reset the attempts

if st.button('Restart Game'):
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("Game restarted! Try guessing a new number.")