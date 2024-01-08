import random
from tkinter import *


# def for checking if word exists in the wordlist

with open("wordList.txt") as f:
        mylist = list(f)

wordList = [] # contains the list of all valid words

for words in mylist:
    wordList.append(words.strip())


genList = list((random.choice(wordList)).upper()) # contains the word to guess in a list 
print(genList)


def presentInList(word):

    
    if(word in wordList):
        return True
    return False



# def for checking is the input word is not empty or invalid and has length of 5

def isValid(word):

    if len(word) == 5 and presentInList(word):      
        return True
    return False

# def for changing the subheading to "enter word", "you lose" , "you won"

inputCounter=0
name="User"

def change_heading():
    
    global inputCounter
    global name
    check_word=inputBox.get()

    if inputCounter==0:
        name = inputBox.get()
        subLabel.config(text=name + " ! Enter your Guess word")
        inputCounter+=1
    
    elif inputCounter==6 and isValid(check_word) :
        subLabel.config(text="YOU LOSE!")
        enterButton.config(DISABLED)

    elif isValid(check_word):
        subLabel.config(text=name + " ! Enter your Guess word")
        inputCounter+=1
    else:
        subLabel.config(text="Word not found in wordlist. Enter another word!")


    
# def for updating the labels


def updateLabels(inputWord):
    
    inputWord.strip()
    inputWord = inputWord.upper()
    userList = list(inputWord)

    for col in range(5):
        exec(f"label_{inputCounter-1}_{col}.config(text=inputWord[col])")

        #print(userList[col] +"  "+ genList[col]+"\n")

        if userList[col] == genList[col]:
            exec(f"label_{inputCounter-1}_{col}.config(bg=box_green,fg=white)")
        elif userList[col] in genList:
            exec(f"label_{inputCounter-1}_{col}.config(bg=box_yellow,fg=white)")
        else:
            exec(f"label_{inputCounter-1}_{col}.config(bg=box_grey,fg=white)")

    winCheck(userList,genList)
        
# def for performing all functions

def allFunctions(inputWord):
    
    
    if inputCounter in range(1,8) and isValid(inputWord):
        updateLabels(inputWord)

    change_heading()

# def for checking winning condition
    
def winCheck(userList,genList):

    print(userList == genList)

    if(userList == genList):
        subLabel.config(text="CONGRATULATIONS! YOU WON")
        enterButton.config(DISABLED)




# The UI of Wordle Game

box_green = "#79B851"
box_yellow = "#F3C237"
box_grey = "#A4AEC4"


black = "#15141A"
yellow = "#F8CF2C"
red = "#AB202A"
white = "#FFFFFF"
my_font="Roboto"
grey="#335155"

root = Tk()
root.title("Wordle Game")
root.config(background=black)

wordleLabel = Label(root,text = "Wordle",font=(my_font,50),bg=black,fg=yellow)
wordleLabel.pack(pady=5)

subLabel = Label(root,text="Enter Player Name",font=(my_font,20),bg=black,fg=red)
subLabel.pack(pady=5)

inputBox = Entry(root, font=(my_font,10),borderwidth="3",relief="flat",bg=grey,fg=white)
inputBox.pack(pady=10)

enterButton = Button(root,font=(my_font, 16),text="Submit", command=lambda:allFunctions(inputBox.get()),bg=yellow,fg=black)
enterButton.pack(pady=10)

# The Labels that contains each letter of words

box_width = 2
box_height = 1
box_borderwidth = 1
box_relief = "solid"
box_bg = "#335155"
box_fg = "#FFFFFF"
box_font = ("Roboto", 20)

x_start = 250  # x-coordinate of labels
y_start = 250  # y-coordinate of labels

for row in range(6):
    ybox = y_start + row * 40
    for col in range(5):
        xbox = x_start + col * 40
        text = " "
        
        exec(f"label_{row}_{col} = Label(root, borderwidth=box_borderwidth, relief=box_relief, bg=box_bg, fg=box_fg,height=box_height, width=box_width, text=text, font=box_font)")
        exec(f"label_{row}_{col}.place(x=xbox, y=ybox)")


root.geometry("700x500")
root.resizable(False,False)
root.mainloop()


