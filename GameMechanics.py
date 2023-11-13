from tkinter import *

# def for checking is the input word is not empty or invalid and has length of 5

def isValid(word):
    if len(word) == 5:
        return True
    return False

# def for changing the subheading to "enter word", "you lose" , "you won"

inputCounter=0

def changeSubheading():
    global inputCounter

    check_word=inputBox.get()


    if inputCounter==0:
        subLabel.config(text="Enter Guess words")
        inputCounter+=1
    
    elif inputCounter==6  and isValid(check_word) :
        subLabel.config(text="YOU LOSE!")
        enterButton.config(DISABLED)

    elif isValid(check_word) :
        print(check_word)
        inputCounter+=1

    
# def for updating the labels

def updateLabels(word):

    global wordCount

    for i in range(5):
        labels[wordCount].config(text=word[i])
    
  


# The UI of Wordle Game

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

enterButton = Button(root,font=(my_font, 16),text="Submit", command=changeSubheading,bg=yellow,fg=black)
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
y_start = 250  # y-coordinate of labelsS

labels = []

for row in range(6):
    ybox = y_start + row * 40
    for col in range(5):
        xbox = x_start + col * 40
        text = " "

        label = Label(root, borderwidth=box_borderwidth, relief=box_relief, bg=box_bg, fg=box_fg,
                      height=box_height, width=box_width, text=text, font=box_font)
        label.place(x=xbox, y=ybox)

        labels.append(label)



root.geometry("700x500")
root.resizable(False,False)
root.mainloop()

