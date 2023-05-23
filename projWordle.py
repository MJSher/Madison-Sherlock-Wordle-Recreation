# Name:        Madison Sherlock
# Class:       CSC 110 - Spring 2022
# Assignment:  Programming Project Implementation
# Due Date:    May 2, 2022

# Program Title: Wordle

# Project Description:
# --------------------
""" This problem will play the game Wordle with one player. The game
starts off with a random 5 letter word, and the player has to guess what said
word is, and with each guess, a clue is given in the form of a 5-character code
consisting of only Xs, Ys, and Gs corresponding with your input word. and X
means that the letter in that same position is never in the word, a Y means
that the letter in that same position is in the word, but in the wrong
position, and a G means the letter in that position is in the word and in that
position. The player has 6 different attempts to guess the word, and if they
are unable to guess it in those tries, the game ends, and the player has to
restart the game"""

# General Solution:
# -----------------
"""
get the data from five-letter-words.csv and put it into a list of words. When
the player makes a guess, (and if the word is in in the list of
five-letter-words.csv), the program then goes through the input guess, and checks
to see if each character is a part of the word being guessed (uses linear
search), then making a new string to return. if an character of your input
guess is not found in the original word, the clue string is added X to that point.
If the character is found in the list but not at the same index, the clue string
is added Y to its string, and if the character is in the original word and at
the same index, it inputs G to the output string. once that is completed, the
program outputs the clue and the number of guesses increases by 1. This repeats
until the word is guessed or the number of guesses goes to 6. The game is won
if the former happens, and the game is lost if the latter happens. Both results
should print the score
"""
#-----------------
import random
#essentially plays the entire game of wordle. All functions besides main
    #will be called in this function.
def playWordle(wordsList, overallScore):
    #this allows the user to play the game again if they want to.
    #(so in main, there will be a while loop saying "while keepPlaying == True")
    #if you lose, your score will be 10
    #guessWordsList is used so that once worldWord is chosen, the same word will not be chosen twice
    worldWord = randomWord(wordsList)
    isValid = False
    wordGuessed = False
    isWin = False
    counter = 0
    capitalInputWord = ""
    while isWin == False and counter < 6:
        while isValid == False:
            inputWord = input("Make a guess: ")
            capitalInputWord = inputWord.upper()
            isValid = checkWordinDictionary(capitalInputWord, wordsList)
            if isValid == False:
                print ("Word not in dictionary - try again...")
        print(capitalInputWord)
        isWin = checkInput(capitalInputWord, worldWord)
        counter = counter + 1
        overallScore = overallScore + 1
        isValid = False
    if isWin == True:
        print ("Congratulations, your wordle score for this game is ", counter)
    if isWin == False:
        overallScore = (overallScore - 6 + 10)
        print ("Sorry, you did not guess the word: ", worldWord)
    print ("Your overall score is ", overallScore)
    
    return overallScore
    
    

#Function to get the data from the file and put it into an array
    #asks user for filename (makes sure that the file name is valid)
    #sorts the data from five-letter-words into an array
def getData():
    validFile = False
    while validFile == False:
        fname = input("Please enter a file name: ")
        try:
            inFile = open(fname, "r")
            validFile = True
        except IOError:
            print("Invalid file name try again...")
    wordsList = []
    line = "b"
    while line != "":
        line = inFile.readline()
        line = line.strip()
        wordsList.append(line)
    inFile.close()
    return wordsList

#Function to get a random word for the player to guess
#reminder that, while wordsList is used as a parameter, it is called using guessWordsList, not WordsList
def randomWord(wordsList):
    randomNum = random.randint(0, (len(wordsList) - 1))
    worldWord = wordsList[randomNum]
    return worldWord

#checks to see if the input word is part of the dictionary in wordsList. If so, it returns true.
def checkWordinDictionary(inputWord, wordsList):
    left = 0
    right = (len(wordsList) - 1)
    found = False
    mid = 0
    while found == False and right >= left:
        mid = ((left + right) // 2)
        if inputWord > wordsList[mid]:
            left = mid + 1
        elif inputWord < wordsList[mid]:
            right = mid - 1
        else:
            found = True
        if right == 1:
            found = True
    return found

#Function to check if the word is guessed correctly (outputs that XYG clue too)
#looks at every letter in inputWord and sees if it matches worldWord. It then returns a clue based on whether it is the same letter and/or at the same index
#(WorldWord is the word randomly generated, while inputWord is the word the user inputs)
def checkInput(inputWord, worldWord):
    clue = "XXXXX"
    isWin = False
    if inputWord == worldWord:
        clue = "GGGGG"
        
    for i in range(len(worldWord)):
        if inputWord[i] == worldWord[i]:
            clue = clue[:(i)] + "G" + clue [(i + 1) :]
            worldWord = worldWord[:(i)] + "_" + worldWord [(i + 1) :]
    for j in range(len(inputWord)):
        if inputWord[j] in worldWord:
            if clue[j] != "G":
                clue = clue[:(j)] + "Y" + clue [(j + 1) :]
    if clue == "GGGGG":
        isWin = True
        print(clue)
    else:
        isWin = False
        print(clue)
    return isWin

#calls play Wordle, and asks if the user wants to play again.
def main(seedIn):
    random.seed(seedIn)
    wordsList = getData()
    overallScore = 0
    keepPlaying = "Y"
    answeredCorrectly = False
    while keepPlaying == "Y" or keepPlaying == "y":
        keepPlaying = ""
        overallScore = playWordle(wordsList, overallScore)
        keepPlaying = (input("Would you like to play again (Y or N)? "))
        if keepPlaying == "Y" or keepPlaying == "y":
            answeredCorrectly = True
        elif keepPlaying == "N" or keepPlaying == "n":
            answeredCorrectly = True
            print("Thanks for playing!")
        else:
            print("Invalid entry, try again...")
