import json

##open files##
with open('list.json') as json_data:    
    dataList = json.load(json_data)
with open('dict.json') as json_data:    
    dataDict = json.load(json_data)


originalTextOutput = open("originalTextOutput.txt", "w")
for elmt in dataList:
    for key, value in dataDict.items():
        if int(key) == elmt:
            print(value)
            originalTextOutput.write(value)
            originalTextOutput.write(' ')

originalTextOutput.close()
