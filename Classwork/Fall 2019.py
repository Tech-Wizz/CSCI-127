def create_list(amount):
    on = 0
    x, y = 1,2 
    while on<amount:
        on += 1
        print(x, end=",")
        x, y = y, y+1
        

how_many = int(input("Enter the number of integers the list should contain:"))
numbers = create_list(how_many)
print(numbers)
