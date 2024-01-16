import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Program 6                            |
# December 3, 2019                                |
# Kruize Christensen                              |
# -------------------------------------------------

games = pd.read_csv('video_games.csv')
plt.figure("Video Game Information")

#-----------------------------------------------------------

for i in range(len(games)):
    year = games.loc[i, "Release.Year"]

plt.subplot(121)
plt.title("Release Year")

games["Release.Year"].value_counts().plot.pie(startangle=90)

#-----------------------------------------------------------
for i in range(len(games)):
    year = games.loc[i, "Release.Rating"]

plt.subplot(122)
plt.xlabel("Rating")
plt.ylabel("Number of Games")
plt.title("Games Ratings 2006-2008")

games["Release.Rating"].value_counts(sort=False).plot("bar", color=("Red"))
#----------------------------------------------------------
plt.show()
