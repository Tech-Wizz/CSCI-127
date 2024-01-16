def list_reverse_iterative (alist):
    result = []
    for index in range(len(alist) -1, -1,-1):
        result.append(alist[index])
    return result

def list_reverse_iterative2 (alist):
    result = []
    for item in alist:
        result = [item] + result
    return result

def list_reverse_recursive (alist):
    if alist == []:
        return alist
    else:
        return list_reverse_recursive(alist[1:]) + [alist[0]]

def list_reverse_recursive2 (alist):
    if alist == []:
        return alist
    else:
        return [alist[-1]] + list_reverse_recursive(alist[:-1])

days = ["mon", "tues", "wed", "thursday"]
print("Iterative 1 is", list_reverse_iterative(days))
print("Iterative 2 is", list_reverse_iterative2(days))
print("Recursive 1 is", list_reverse_recursive(days))
print("Recursive 2 is",list_reverse_recursive2(days))
