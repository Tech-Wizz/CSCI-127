def calculate(file):
    doc = open(file,"r")
    input_line = doc.readline()
    while input_line:
        values = input_line.split()
        cumulative_population = cumulative_population + int(values[1])
        summary_file.write(str(cumulative_population) + "\n")
        input_line = census_file.readline()
    print(input_line)


Type= int(input("Enter in Euro:"))


calculate("currency.txt")
