from tkinter import *

def find():
    newSentence = sentence.get()
    newKeyword = word.get()
    output = []
    sentenceList = newSentence.split(' ')

    if newKeyword in sentenceList:
    #finds the position(s) of the words
        for (i, subword) in enumerate(sentenceList):
            if (subword == newKeyword):
                output.append(i+1) #+1 fixes starting at zero
        outputLabel = Label(window, text=output).pack()
    else:
        errorLabel = Label(window, text="That is not in the sentance, try again!").pack()

window = Tk()
window.title("Position checker")
#window.maxsize(width=860, height=480)
window.minsize(width=400, height=200)

sentence= StringVar()
word= StringVar()

titleLabel = Label(window, text="Insert your text here: ", font="none 12").pack()

sentenceEntry = Entry(window, width=50, textvariable=sentence).pack()

infoLabel = Label(window, text="Type word you want to find here: ", font="none 12").pack()

wordEntry = Entry(window, width=30, textvariable=word).pack()

convertButton = Button(window, text = "Find", command = find, fg = 'white', bg= 'grey', font="none 12").pack()
