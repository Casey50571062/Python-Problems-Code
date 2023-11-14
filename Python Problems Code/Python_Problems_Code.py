import math as mh

def vowel_count(x):
    count=0
    vowel=["a","e","i","o","u","A","E","I","O","U"]
    for length in x:
        for y in vowel:
            if length == y:
                count+=1
    print(count)
radian = int(input("Enter your radian you'd like to convert to a degree: "))
degree = (radian*180)/mh.pi
print(f"Your degree is {degree}")

sortlist = []
print("\nWE CAN sort your list :3")
length = int(input("How many items are in your list: "))
for x in range(length):
    item = int(input("Enter one of your items: "))
    sortlist.append(item)
style = input("sort by asc or desc: ").lower()
if style == "asc":
    sortlist.sort()
    print(sortlist)
elif style == "desc":
    sortlist.sort()
    sortlist.reverse()
    print(sortlist)
else:
    print("YOU CANT SPELL!, or you dont want it changed which is fine.")
    print(sortlist)

binary = int(input("Enter a whole number value below 1024 to convert: "))
print(bin(binary).replace("0b",""))

wordNeeded = input("enter a word to start a vowel count :3 ")
vowel_count(wordNeeded)

creditCard = input("John Wick needs your help against the epic fortnite sweats and only YOU can save him, Please enter your parents credit card number to help John Wick gets his epic VICTORY ROYALE: ")
print(creditCard[len(creditCard)-4:])

xCount=0
yCount=0
equalXY=False
xoro = input("Please enter your x or o value: ")
for num in range(0,len(xoro)):
    lett=(xoro[num])
    if lett == "x"or lett=="X":
        xCount+=1
    elif lett == "y"or lett=="Y":
        yCount+=1
if yCount == xCount:
    equalXY=True
else:
    equalXY=False
print(equalXY)

num1 = int(input("Enter a num: "))
mathcalc = input("Enter a mathimatical operator between; +, -, /, *: ")
num2 = int(input("Enter you second num: "))
match mathcalc:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "/":
        print(num1 / num2)
    case "*":
        print(num1 * num2)

fullPrice = int(input("\nPlease enter your full price: "))
discount = int(input("Please enter your discount: "))
print(f"Your total is {fullPrice - (fullPrice * (discount/100))}")

x=0
newList = []
print("\nTo stop adding to the list, input a y")
while x != "y":
    x = input("Enter a value to be added to the list: ")
    try:
        int(x)
    except:
        print("String")
    else:
        int(x)
        newList.append(x)
print(newList)

newString = ""
strings = input("Enter a string please :3 ")
for x in range(0,len(strings)):
    newString+=strings[x]+strings[x]
    print(newString)
print(newString)

