"""
Methods file
"""

# Defining Methods
def getWords(numberOfLetters):                                                       # getWords is passed player input int & wordsFound list is intialised
    wordsFound=[]
    fin = open("words.txt")                                                          # words.txt file is opened and assigned to fin, looping over each entry and striped for validation
    for line in fin:
        word = line.strip()
        if len(word) == numberOfLetters:                                             # If the length of a word matches length of numberOfLetters it's appended to wordsFound list
            wordsFound.append(word)
    fin.close()		                                                                 # File is closed after use, wordsFound list is returned by getWords method
    return wordsFound                        

def replaceAll(guess, word, letter): #guessString, guessWord, thisLetter
    if letter in guess:                                                              # If the player enters a letter already in the guessString, inform the player
        print("You guessed that one already!")
        return guess
    for pos in range(len(guess)):                                                    # For each element in the guessString (the underscores)
        if word[pos] == letter:                                                      # If the letter input by the player matches a letter at the current index of the the guessWord
            guess = guess[:pos] + letter + guess[pos+1:]                             # Replace the underscore with the letter at the same index where the guessWord match was found using slice notation
    return guess                                                                     # Return the updated guessString

def getWordLength():
    numberOfLetters = input("Enter a number between 2 and 21: ")                     # Player enters length of word to be guessed
    while not numberOfLetters.isnumeric():                                           # validate player entry is a number
        numberOfLetters = input("Enter a number between 2 and 21: ")
    while int(numberOfLetters) < 2 or int(numberOfLetters) > 21:                     # validate player entry is between 1 and 22
        numberOfLetters = input("Enter a number between 2 and 21: ")                                                
    return int(numberOfLetters)

def availLetters(alphabet, letter): #alphabet, thisLetter
    for pos in range(len(alphabet)):
        if alphabet[pos] == letter:
            alphabet = alphabet[:pos] + "_" + alphabet[pos+1:]
    return alphabet

def playerWins(score):
    playerName = input("Enter player name: ")                                          # Player enters name
    fin = open("hangmanScores.txt", "r")                                               # Open hangmanScores.txt for reading
    fout = open("hangmanScores.txt", "a")                                              # and appending
    newScoreText = "{}, {}\n".format(playerName, score)                                # Record player scores on 'score board'
    fout.write(newScoreText)
    fin.close()
    fout.close()
