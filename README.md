# Hangman Game

## Overview
This is a command-line Hangman game implemented in Python. The game randomly selects a month of the year as the secret word (can change word list), and the player must guess the word one letter at a time. The player has a limited number of guesses before they lose the game, and each incorrect guess eliminates a part of the hangman's body.

## Features
- **Random Word Selection:** The game randomly chooses a month as the secret word from a predefined list.
- **Hint System:** The current state of the word is displayed after each guess, with unguessed letters shown as `?`.
- **Body Part Elimination:** Each incorrect guess removes one of the hangman's body parts (Head, Left Arm, Right Arm, Left Leg, Right Leg).
- **Win/Loss Condition:** The game ends when the player either guesses the word correctly or runs out of guesses.

## How to Play
1. **Start the Game:** Run the script to begin the game.
2. **Guess a Letter:** When prompted, input a letter you think is in the secret word.
3. **View Progress:** After each guess, you'll see the current hint (with correct guesses filled in) and the number of remaining guesses.
4. **Win the Game:** If you guess all the letters correctly before running out of guesses, you win.
5. **Lose the Game:** If you use all your guesses without completing the word, the game will reveal the secret word.

## Example Usage
```python
Hangman = hangman()
print("welcome to hangman!")
while(Hangman.getWin() == False and Hangman.getGuesses() < 6):
    guess = input("Please enter a letter:  ")
    Hangman.makeHint(guess)
    Hangman.checkWin()
    if Hangman.getWin() == True:
        print("hint = " + str(Hangman.getHint()))
        print("\n\ncongrats, you won, the word was: " + Hangman.getSecret())
    else:
        print("you didn't win yet, guesses remaining = " + str(6 - Hangman.getGuesses()))
        print("Body Parts Eliminated : " + str(Hangman.getBodyParts()))
        print("hint = " + str(Hangman.getHint()) + "\n")
        
if Hangman.getWin() == False and 6 - Hangman.getGuesses() == 0:
    print("\n\nsorry, you lost, the secret word was: " + Hangman.getSecret())
