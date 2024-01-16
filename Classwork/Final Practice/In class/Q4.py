import pandas as pd
data_frame = pd.read_csv("video_games.csv")
year_series = data_frame["Release.Year"].value_counts()
print(year_series)
year = 2019
releases = 1

print("The number of video games released in", year, "is", releases)
