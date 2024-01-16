import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# November 26, 2019                               |
# Kruize Christensen                              |
# -------------------------------------------------


def main(file_name):
    # read the file_name into a pandas dataframe
    file = open(file_name, "r")
    names = []
    number = []
    i = 0
    for data in file:
        LST = data.split(",")
        if i < 1:
            x_axis = LST[0]
            y_axis = LST[-1]
        i += 1
        if i > 1:
            names.append(LST[0])
            number.append(int(LST[-1]))
    
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"
    plt.figure()
    plt.bar(names, number, color=('b','gold'), width=.5)
    plt.title(file_name [:-4])
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom = .25)

    # The only four statements that may use the matplotlib library appear next.
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
