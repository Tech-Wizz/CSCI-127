# --------------------------------------
# CSCI 127, Lab 3                      |
# September 17, 2019                   |
# Kruize Christensen                   |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------

def count_built_in(sentence):
    count=0
    substring = "a"
    vowels = sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u") + sentence.count("A") + sentence.count("E") + sentence.count("I") + sentence.count("O") + sentence.count("U")  
    return vowels

def count_iterative(sentence):
    count=0
    for i in sentence:
        if i in "aeiouAEIOU":
            count += 1
    return count

def count_recursive(sentence):
    vowels = "aeiouAEIOU"
    if (sentence == ""):
        return 0 
    elif sentence[0] in vowels:
        return 1 + count_recursive(sentence[1:])
    else:
        return 0 + count_recursive(sentence[1:])

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
