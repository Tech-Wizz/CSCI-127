import string

def encode(words, shift):
    answer = ""
    words = words.lower()
    for character in words:
        if character in string.ascii_lowercase:
            position = string.ascii_lowercase.index(character)
            position = (position + shift) %26
            answer += string.ascii_lowercase[position]
        elif character in string.ascii_uppercase:
            position = string.ascii_uppercase.index(character)
            position = (position + shift) %26
            answer += string.ascii_uppercase[position]
        else:
            answer += character
    return answer

def main():
    sentence = input("Please enter a sentence to encode: ")
    shift = int(input("Please enter the shift number: "))
    encoded_sentence = encode(sentence, shift)
    print("Result:", encoded_sentence)

main()
