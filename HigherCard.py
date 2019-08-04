# HigherCard.py
# Billy Ridgeway
# Plays a card game called War. User vs. Player.

import random       # Imports the random library.
keep_going = True   # Set the variable to true.
answer = ""         # Sets the answer to [Enter]

# Creates a list of card suits.
suits = ["clubs", "diamonds", "hearts", "spades"]

# Creates a list of the card faces.
faces = ["two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "jack",
         "queen", "king", "ace"]

# Creates a while loop that generates the cards and evaluates
# who won the game. The loop continues as long the user presses Enter.
#  If the user presses any other key the game will exit.
while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("I have the", my_face, "of", my_suit, ".")
    print("You have the", your_face, "of", your_suit, ".")

    if faces.index(my_face) > faces.index(your_face):
        print("I win!")
    elif faces.index(my_face) < faces.index(your_face):
        print("You win!")
    else:
        print("It's a tie!")
    answer = input("Hit [Enter] to keep going, or any key to exit: ")
    keep_going = (answer == "")
