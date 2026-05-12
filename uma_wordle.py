import streamlit as st
import pandas as pd
import numpy as np
import random



UMA_NAMES = [
    "Vodka", "Symboli Rudolf", "Gold Ship", "Oguri Cap",
    "Tokai Teio", "Maruzensky", "Verxina", "Air Groove",
    "Fuji Kiseki", "Grass Wonder", "Daiwa Scarlet",
    "Narita Brian", "Hishi Amazon", "Taiki Shuttle",
    "Special Week", "El Condor Pasa", "Agnes Tachyon",
    "Mejiro McQueen", "Silence Suzuka", "TM Opera O",
    "Winning Ticket", "Wonder Acute", "Yaeno Muteki",
    "Kitasan Black", "Satono Diamond", "Satono Crown",
    "Deep Impact", "Kizuna", "Rey de Oro", "Almond Eye",
    "Stay Gold", "Dream Journey", "Biwa Hayahide", "Kurofune",
    "Orfevre", "Fenomeno", "Daiwa Major", "Admire Moon", "Nakayama Festa",
    "Haru Urara", "Rice Shower", "Mejiro Dober", "Mejiro Ryan", "Mejiro Palmer", 
    "Mejiro Ardan"
]

UMA_NAMES = [name.upper() for name in UMA_NAMES]

max_attempts = 6



#generate answer
if "answer" not in st.session_state:
    st.session_state.answer = random.choice(UMA_NAMES)
if "guesses" not in st.session_state:
    st.session_state.guesses = []



#definintions 

#defintion for displaying blank boxes
def display_blanks(answer):
    normalized = strip_spaces(answer)
    return " ".join(["_"] * len(normalized))

#defintion for stripping spaces and periods from names for comparison
def strip_spaces(name: str) -> str:
    return name.replace(" ", "").replace(".", "")

#guessing check and creating boxes
def guess_check(guess, answer):
    guess = strip_spaces(guess)
    answer = strip_spaces(answer)

    result = ["black"] * len(guess)
    answer_chars = list(answer)

    #generate Greens
    for i in range(len(guess)):
        if i < len(answer) and guess[i] == answer[i]:
            result[i] = "green"
            answer_chars[i] = None

    # generate Yellows
    for i in range(len(guess)):
        if result[i] == "green":
            continue

        if guess[i] in answer_chars:
            result[i] = "yellow"
            answer_chars[answer_chars.index(guess[i])] = None

    return result

#displaying the box at the top of page, the answer is hidden but the number of boxes 
# corresponds to the number of letters in the answer
def display_empty_boxes(answer):
    normalized = strip_spaces(answer)

    cols = st.columns(len(normalized))

    for col in cols:
        col.markdown(
            """
            <div style="
                width:50px;
                height:50px;
                border:3px solid #888;
                border-radius:6px;
                margin:auto;
                background-color:#121213;
            ">
            </div>
            """,
            unsafe_allow_html=True
        )


#Creating the main display of the game, including title, instructions, and input for guesses
st.title("Uma Wordle")
st.subheader("Guess the Uma name in 6 attempts or less.")
st.write(display_blanks(st.session_state.answer))
display_empty_boxes(st.session_state.answer)
guess = st.text_input("Enter your guess (Uma name):").upper()



#button to submit guess, checks if guess is valid and adds to guesses list, also checks if guess is correct and 
# displays success message if correct
if st.button("Submit Guess"):

    if guess:

        # Strip spaces both words
        normalized_guess = strip_spaces(guess)
        normalized_answer = strip_spaces(st.session_state.answer)

        #changing guess length to match answer length, so that the guess check can work properly, 
        # and also so that the colored boxes can be displayed properly
        matched_guess = normalized_guess[:len(normalized_answer)]

        # Store ONLY guesses that match length of answer
        st.session_state.guesses.append(matched_guess)

        # Win check ONLY compares answer length
        if matched_guess == normalized_answer:
            st.success(f"You got it! Answer: {st.session_state.answer}")


 












#This is where the subheader for guesses are, and displays the previous guesses
st.subheader("Guesses:")

for guess in st.session_state.guesses:

    colors = guess_check(guess, st.session_state.answer)

    # Display guess text
    st.write(guess)

    # Display colored boxes
    cols = st.columns(len(colors))

    normalized_guess = strip_spaces(guess)

    for i, col in enumerate(cols):

        color = colors[i]
        letter = normalized_guess[i].upper()

        if color == "green":
            bg = "#6aaa64"
        elif color == "yellow":
            bg = "#c9b458"
        else:
            bg = "#787c7e"

        col.markdown(
            f"""
            <div style="
                background-color:{bg};
                color:white;
                width:40px;
                height:40px;
                text-align:center;
                line-height:40px;
                font-size:24px;
                border-radius:5px;
                margin:auto;
            ">
                {letter}
            </div>
            """,
            unsafe_allow_html=True
        )



    