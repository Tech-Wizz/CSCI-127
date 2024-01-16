# --------------------------------------
# CSCI 127, Lab 4
# September 24, 2019
# Kruize Christensen
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    
    print("-----------------------------")
    possibleOutcomes = []
    maxWins = points_earned//3

    for theMaxWin in range(maxWins, -1, -1):
        totalPoints = [theMaxWin, points_earned - (theMaxWin * 3),0]
        while sum(totalPoints) < games_played:
            totalPoints[2] += 1

        if((totalPoints[0] * 3) + totalPoints[1] == points_earned) and sum(totalPoints) == games_played:
            possibleOutcomes.append(totalPoints)

    for possibility in possibleOutcomes:
        print("{}-{}-{}".format(possibility[0], possibility[1], possibility[2]))
        

    print()

# --------------------------------------

def process_seasons(seasons):
    season = 0
    for i in seasons:
        season = seasons.index(i) + 1
        process_season(season, i[0], i[1])

          
# --------------------------------------

def main():
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()
