"""
Hangman played through terminal
""" 
import random
import methods                                                                         # Importing game methods from methods.py

# Initialise required variables
print("----------------")
print("GAME START")
numberOfLetters = methods.getWordLength()                                              # Player enters length of word to be guessed
words = methods.getWords(numberOfLetters)                                              # Initialising word with getWords method with argument passed
print(f"There are {len(words)} words with {numberOfLetters} letters, good luck!")      # Displaying how many words with the length of the number chosen by player

guessWord = words[random.randint(0,len(words)-1)]                                      # Initialising the word to guess this game is randomly selected
print(f"(dev) guessWord: {guessWord}")                                                 # Displaying guessWord to dev purposes

lives = 6                                                                              # Initialising number of guesses
guessString = "_" * numberOfLetters                                                    # Initialising empty guess string of underscores
alphabet = "abcdrfghijklmnopqrstuvwyxz"                                                # Initialising alphabet letters currently not guessed

# Main / game loop
while lives > 0:
    thisLetter = input("Guess a letter: ").lower()                                     # All entries myst be lower case as all words in word.txt are in lowercase
    if len(thisLetter) > 1:                                                            # Validation for only one letter to be guessed
        continue
    elif not thisLetter.isalpha():                                                     # Validation to ensure player entry is letter
        continue
    elif thisLetter in guessWord:
        guessString = methods.replaceAll(guessString,guessWord,thisLetter)
        if guessString == guessWord:
            print("----------------")
            print(f"Congratulations! You guessed the word! It was '{guessString.upper()}'!")
            score = lives * numberOfLetters
            print(f"You scored: {score}")
            break
    else:
        lives = lives-1
        print(f"Ouch, that wasn't right - lost a life!")
    print("----------------")
    print("Current guess: " + guessString)
    print(f"Lives: {str(lives)}")
    options = methods.availLetters(alphabet, thisLetter)
    print("Letters available: " + options)
    alphabet = options

# If the player guesses the word with lives greater than 0
if lives > 0:
    methods.playerWins(score)
    
# If the player runs out of lives, then display 'Game Over' and reveal the word, ending the game
if lives == 0:
    print(f"Game Over! The word was '{guessWord.upper()}'!")