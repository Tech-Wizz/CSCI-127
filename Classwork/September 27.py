def smallest_binary_number(number):
    answer = 1
    while answer < number:
        answer *= 2
    return answer

def main():
    input_file = open("../binarize.in", "r")
    output_file = open("binarize.out", "w")

    how_many = int(input_file.readline())

    for i in range(how_many):
        number_to_binarize = int(input_file.readline())
        output_file.write("Input Value: " + str(number_to_binarize) + "\n")
        result = smallest_binary_number(number_to_binarize)
        output_file.write(str(result) + "\n\n"


    input_file.close()
    output_file.close()   #super important to close output files!


