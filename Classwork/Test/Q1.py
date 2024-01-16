def grocery_bill(file_name):

    input_file = open(file_name)

    for line in input_file:
        data = line.split(",")
        cost = 0
        adding = cost + int(data[1])
        prosses = line[:-1] + "," + str(average) + "\n"
        print(prosses)

    input_file.close()
        
grocery_bill("town-and-country.cvs")
