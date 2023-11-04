import random
from spellchecker import SpellChecker
spell = SpellChecker()
from colorama import Fore

def newWord():
    with open("/home/reek/Desktop/WordleGame/GameMech/wordList.txt") as f:
        mylist = list(f)
    word = random.choice(mylist)
    genList = creating_list(word)
    print(genList)
    return genList 

def takeInput():
    userWord = input("")
    if len(userWord) != 5:
        print("Must be 5 letters")
    else:
        userList = check_word_spelling(userWord)
        return userList

def check_word_spelling(word):
    corrected_word = spell.correction(word)
    if word == corrected_word:
        userList = creating_list(word)
        return userList
    else:
        print("Not a valid word!")
        return []  # Return an empty list to indicate an invalid word

def creating_list(word):
    s = list(word.strip())
    return s

def compare(genList, userList):
    if len(genList) != len(userList):
        print("Both lists must have the same length.")
        return

    for i in range(0, len(genList)):
        if userList[i] != genList[i]:
            print(Fore.CYAN + userList[i], end="")

gl = newWord()
ul = takeInput()
compare(gl, ul)
