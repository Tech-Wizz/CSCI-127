def function1(data):   #market dominance by console
    consoles = {}
    for line in data:
        line = line.split(',')
        console = line[-24]
        if console in consoles.keys():
            consoles[console] +=1
        else:
            consoles[console] = 1
    total = 0
    for item in consoles.keys():
        total += consoles[item]
    print('Market dominance by console:\n------------------------------------\n')
    for item in consoles.keys():
        print ('{}: {:.2f}%'.format(item, (consoles[item]/total)*100))


def function2(data): #most and least play time
    length = {}
    max = [0]
    min = [100000]
    maxTitle = []
    minTitle = []
    for line in data:
        line = line.split(',')
        print(line[-5])
        length = float(line[-5])
        if length >= max[1]:
            max = [length]
            maxTitle = line[0]
        elif length <= min[1]:
            min = [length]
            minTitle = [length[0]]
    print("The game with the most story time is: {} with {} hours".format(max[0], max[1]))
    print("The game with the least story time is: {} with {} hours".format(min[0], min[1]))
    


def function3(data):  #reviews by developer
    devs = {}
    total = 0
    n = 0
    results = []
    for line in data:
        line = line.split(',')
        dev = line[-29]
        review = line[-27]
        if dev not in devs:
            devs[dev] = []
        devs[dev] += review
    for dev in devs.keys():
        for value in devs[dev]:
            total += int(value)
            n += 1
        mean = total / n
        results += [mean, dev]
    results.sort()
    print('List of developers by average reviews')
    for i in range(1, len(results)):
        print('{}. {} has an average review score of {}'.format(i, results[i-1][1], results[i-1][0]))


    

def main(file):
    data = open(file, 'r')
    data.readline()
    function1(data)

    print('\n\n')

    data = open(file, 'r')
    data.readline()
    function2(data)

    print('\n\n')

    data = open(file, 'r')
    data.readline()
    function3(data)
    data.close()



main('video_games.csv')
def main(file):
    data = open(file, 'r')
    data.readline()
    function1(data)

    print('\n\n')

    # data = open(file, 'r')
    # data.readline()
    # function2(data)

    print('\n\n')

    data = open(file, 'r')
    data.readline()
    function3(data)
    data.close()



main('video_games.csv')