def create_dictionary():
    dictionary = {}
    dictionary["sir"] = "matey"
    dictionary["professor"] = "foul blaggert"
    dictionary["hotel"] = "fleabag inn"
    dictionary["student"] = "swabbie"
    dictionary["boy"] = "matey"
    dictionary["madam"] = "proud beauty"
    dictionary["restaurant"] = "galley"
    dictionary["your"] = "yer"
    dictionary["excuse"] = "arr"
    dictionary["students"] = "swabbies"
    dictionary["are"] = "be"
    dictionary["lawyer"] = "foul"

    return dictionary

#-----------------

def translate(dictionary, sentence):
    words = sentence.split()
    for word in words:
        if word in dictionary.keys():
            result += dictionary[word] + " "
        else:
            result += word + " "
    return result 

#---------------------

    def main():
        piratese = create_dictionary()
        sentence = input("Enter sentence to translate: ")
        sentence = sentence.lower()
        translated_sentence = translate(piratese, sentence)
        print(translated_sentence)

    main()