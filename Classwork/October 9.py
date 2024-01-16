import string

# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

# ---------------------------

def create_dictionary(text):
    dictonary = {}
    for letter in string.ascii_lowercase:
        dictonary[letter] += 0
    for letter in text:
        dictonary[letter] += 1
    return dictonary

# ---------------------------

text = keep_letters("raven.txt")
print(text)
        