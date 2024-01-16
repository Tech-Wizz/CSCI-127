import string

# --------------------------------

def sentence_to_words(sentence):
    sentence = sentence.lower()
    reduced_sentence = ""
    for character in sentence:
        if character in string.ascii_lowercase or character == " ":
            reduced_sentence += character
    return reduced_sentence

# --------------------------------

def update(dictionary, words):
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

# --------------------------------

def most_frequent(dictionary):
    most_frequent_word = "EMPTY DICTIONARY"
    largest_count = 0
    for word, count in dictionary.items():
    print("Print the most frequently occuring word, as well as its frequency")

# --------------------------------

def main():
    proceed = "yes"
    word_dictionary = {}
    while proceed == "yes" or proceed == "y":
        sentence = input("Please enter a sentence: ")
        words = sentence_to_words(sentence)
        word_list = words.split()
        update(word_dictionary, word_list)
        print(word_dictionary)
        most_frequent(word_dictionary)
        proceed = input("Would you like to continue? ")
        proceed = proceed.lower()

# --------------------------------

main()

