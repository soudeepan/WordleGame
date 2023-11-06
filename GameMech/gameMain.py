import random
from spellchecker import SpellChecker
spell = SpellChecker()
from colorama import Fore,Back  #Module to import the color

def newWord():   #Function to generate new Word          
    with open("/home/reek/Desktop/WordleGame/GameMech/wordList.txt") as f:
        mylist = list(f)
    word = random.choice(mylist)
    print(word)
    genList = creating_list(word)  # Calling the creating list
    print(genList)
    return genList 
    #Returns the list for the generated word

def takeInput():
    userWord = input("")
    if len(userWord) != 5:
        print("Must be 5 letters")   #If length is not 5 call the function again
    else:
        userList = check_word_spelling(userWord)
        return userList    #return userList

def check_word_spelling(word):
    corrected_word = spell.correction(word)
    if word == corrected_word:
        userList = creating_list(word)
        return userList
    else:
        print("Not a valid word!")
        return []  # Return an empty list to indicate an invalid word

def creating_list(word):
    s = list(word.strip()) #Strip removes the nextline 
    return s

def compare(genList, userList):  #Function for comparing
    if len(genList) != len(userList):
        print("Both lists must have the same length.")
    else :    
        for user_item in userList:
            not_present = True
            for gen_item in genList:
                if user_item == gen_item:
                    not_present = False
                    break
            if not_present:
                print(Fore.CYAN + user_item, end=" ")

gl = newWord()#genList
ul = takeInput()#userList
compare(gl, ul)
