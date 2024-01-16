def determine_winner(teams):
    best_team = "UNKNOWN"
    best_team_wins = 0
    for team, wins in teams.items():
        if wins>best_team_wins:
            best_team = team
            best_team_wins = wins
    return best_team

nl_east = {}
nl_east["WN"]=93
nl_east["PP"]=81
nl_east["AB"]=97
nl_east["NYM"]=86
nl_east["MM"]=57
nl_west={}


    
 
print("NL East Winner: ", determine_winner(nl_east))
print("NL West Winner: ", determine_winner(nl_west))
