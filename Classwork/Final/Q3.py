import numpy as np

def minor_diagonal(value):
    result = 0
    r=1
    c=0
    while c < (size+1):
        result =+ value[:(size-size+r), ::(-size-c)]
        r+=1
        c+=1
    return result 

size = int(input("Enter a positive integer:"))
numbers = np.random.randint(0,11,size*size)
numbers.resize(size,size)
print(numbers)
print("Minor diagonal sum =", minor_diagonal(numbers))





