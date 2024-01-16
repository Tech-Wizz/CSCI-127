
def main(input_file_name, output_file_name):
    
    output_file = open(output_file_name, "w")
    input_file = open(input_file_name, "r")
    
    line = input_file.readline()
    line = line[:-1] + ", Average"
    output_file.write(line)
    
    for line in input_file:
        data = line.split(",")
        score_1 = int(data[1])
        score_2 = int(data[2])
        average = (score_1 + score_2) / 2
        new_line = line[:-1] + "," + str(average) + "\n"
        print(new_line)
        output_file.write(new_line)

    input_file.close()
    output_file.close()


main("grades.csv", "grades2.csv")
