def count_fives (alist):
    result = 0
    for name in alist:
        if len(name) == 5:
               result += 1
    return result

names = ["Reese", "Mike", "Cole", "Kate", "Maria", "Hunter"]
answer = count_fives(names)
print(answer)
