import numpy as np

size = int(input("Enter the size of the n by n board: "))
checkers = np.ndarray(size*size, dtype = "int")
checkers = checkers.reshape(size, size)
checkers[:,:] = 0
checkers[::2, 1::2] = 1
checkers[1::2, ::2] = 1

print(checkers)
