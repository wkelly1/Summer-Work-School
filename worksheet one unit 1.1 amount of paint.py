command = True
while command:
    try:
        size = input("How large are your walls in square meters? ")
        size = float(size)
        command = False
    except ValueError:
        print("This is not a number")
        
command = True
while command:
    try:
        unpaintable = input("How large are the areas that you dont want painting in square meters? ")
        unpaintable = float(unpaintable)
        command = False
    except ValueError:
        print("This is not a number")

command = True
while command:
    try:
        nolayers = input("How many layers do you want? ")
        nolayers = float(nolayers)
        command = False
        
    except ValueError:
        print("This is not a number")

def amountofpaint(a,b,c):
    amountofpaint = ((a - b) * c) / 11
    return(amountofpaint)





print("You need", round(amountofpaint(size, unpaintable, nolayers), 3), "litres of paint")
