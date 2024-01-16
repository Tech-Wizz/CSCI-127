def hanoi (number_disks, start, intermediate, goal):
    Move = 0
    if number_disks >= 1:
        hanoi(number_disks-1, start, goal, intermediate)
        Move+=1
        print("Move ", Move, " disk", number_disks, "from", start, "to",goal)
        hanoi(number_disks-1, intermediate, start, goal)
