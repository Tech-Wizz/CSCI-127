import pandas as pd
import matplotlib.pyplot as plt
import sys          # to determine Python version number
import matplotlib   # to determine Matplotlib version number

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print()

# Create Data --------------------------

# http://www.onthesnow.com/montana/bridger-bowl/historical-snowfall.html
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]   # bridger bowl year
total_snowfall = [253, 304, 388, 265, 283, 209, 194, 271, 177]   # inches
largest_snowfall = [19, 16, 19, 25, 20, 14, 13, 20, 15]          # inches

BridgerDataSet = list(zip(years, total_snowfall, largest_snowfall))
print("BridgerDataSet:", BridgerDataSet, "\n")

data = pd.DataFrame(data = BridgerDataSet, columns=["Year", "Total", "Largest"])
print("Bridger DataFrame")
print("-----------------")
print(data)

data.to_csv('bridger.csv',index=False,header=False)

# Get Data -----------------------------

bridger = pd.read_csv('bridger.csv', names=['Year', 'Total', 'Largest'])
print("\nBridger DataFrame after reading csv file")
print("----------------------------------------")
print(bridger)

# Prepare Data -------------------------

if (bridger.Total.dtype == 'int64'):
    print("\nTotal snowfall is of type int64")
else:
    print("\nTotal Snowfall is of type", bridger.Total.dtype)

# Analyze Data -------------------------

sorted_data = bridger.sort_values(['Total'], ascending=False)
print("\nSorted Bridger Data Set")
print("-----------------------")
print(sorted_data)

print("\nThe least total snowfall was", bridger['Total'].min())

# Display Data -------------------------

bridger.plot(x="Year", y="Total", kind="bar", color="yellow")
plt.xlabel("Year")
plt.ylabel("Total Snowfall")
plt.show()
