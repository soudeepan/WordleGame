import random
from colorama import Fore  #Module to import the color


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
        userList = creating_list(userWord)
        return userList    #return userList

def creating_list(word):
    s = list(word.strip()) #Strip removes the nextline 
    return s

def compare(genList, userList):
    if len(genList) != len(userList):
        print("Both lists must have the same length.")
        return

    correct_positions = 0
    correct_characters = 0
    incorrect_characters = []

    for i in range(len(genList)):
        if userList[i] == genList[i]:
            correct_positions += 1
            print(Fore.GREEN + userList[i], end=" ")
        elif userList[i] in genList:
            correct_characters += 1
            print(Fore.YELLOW + userList[i], end=" ")
        else:
            incorrect_characters.append(userList[i])
            print(Fore.CYAN + userList[i], end=" ")


gl = newWord()#genList
ul = takeInput()#userList
compare(gl, ul)
