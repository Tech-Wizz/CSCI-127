def function2(data): #most and least play time
    length = {}
    max = ['', 0]
    min = ['', 100000]
    for line in data:
        line = line.split(',')
        length = float(line[-5])
        if length >= max[1]:
            max = [line[0], length]
        elif length <= min[1]:
            min = [length[0], length]
    print("The game with the most story time is: {} with {} hours".format(max[0], max[1]))
    print("The game with the least story time is: {} with {} hours".format(min[0], min[1]))




def main(file):
    data = open(file, 'r')
    data.readline()
    function2(data)





main('video_games.csv')