##for i in range(100,0,-1):
##    print(i)

#print the number 1-20 and determine if even or odd

##for i in range(1,21):
##    if i % 2 == 0:
##        print(i,"is even")
##    if i % 2 !=0:
##        print(i,"is odd")

##word = "CSCI 127"
##for eachLetter in word:
##    print(eachLetter)

##myList = ["Joe","Jane","Reese"]
##for eachIteam in myList:
##    print(eachIteam)

##x=0
##while(x<25):
##    print(x)
##    x=x+1

##for i in range(10):
##    if(i ==5):
##        break
##    print(i)


##import random
##
##answer = random.randint(1,10)
##guess = 0
##numOfGuesses = 0
##while(guess != answer):
##    guess = int(input("Your guess?"))
##    numOfGuesses += 1
##
##print("You got it. That took",numOfGuesses,"guesses")

import random
rows = int(input("How many rows?"))
cols = int(input("How many cols?"))
rowText = ""

for c in range(rows):
    rowText = ""
    for i in range(cols):
        ranNum = random.randint(1,2)
        if(ranNum == 1):
            rowText += "*"
        if(ranNum == 2):
            rowText += "-"

print(rowText)
           
