import nltk
from nltk.tokenize import word_tokenize
import json

#open files
#text_file = open("output.txt", "w")
inputText = open("inputText.txt")

#read the file and put into a variable
text = inputText.read()
inputText.close()

#splits the sentence and removes the duplicates leaving it in order
words = text.split(' ')
"""words = word_tokenize(text)"""
removeDuplicates = sorted(set(words), key=words.index)

#gives values to list
new_dict = dict(enumerate(removeDuplicates))
print(new_dict)

#creates an empty list
newList = []

#creates the number sequence by compairing items in the list to the items in the dictionary and prints out the corrosponding character
for elmt in words:
    for key, value in new_dict.items():
        if value == elmt:
            print(key, value)
            newList.append(key)

#prints it as a list
"""text_file.write("\n")
text_file.write(str(newList))
print(newList)

#writing the dictionary to the file
readablestring = str(new_dict)
text_file.write("\n")
text_file.write(readablestring)
#close the file
text_file.close()
"""
with open('list.json', 'w') as outfile:
    json.dump(newList, outfile)
with open('dict.json', 'w') as outfile:
    json.dump(new_dict, outfile)




