def do_something(n):
    if n > 0:           # base case is n <= 0,
        print(n)        # general case is n > 0
        do_something(n-1)

def fibonacci(n):
    if n == 0:          #base case
        return 0
    elif n == 1:        #base case
        return 1
    else:               #general case
        return fibonacci (n-1) + fibonacci (n-2)

def recursive_length (some_string):
    if some_string == "":    #base case
        return 0
    else:                    # general case
        return 1 + recursive_length(some_string[:-1])
