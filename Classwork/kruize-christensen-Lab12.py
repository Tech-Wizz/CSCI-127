import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 19, 2019                               |
# Kruize Christensen                              |
# -------------------------------------------------

def read_file(file_name):
    file = open(file_name, "r")
    college_names = []
    college_enrollments = []
    i = 0
    for data in file:
        LST = data.split(",")
        i += 1
        if i > 1:
            college_names.append(LST[0])
            college_enrollments.append(int(LST[-1]))
        
    return (college_names,college_enrollments)

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)

    plt.figure('Montana State University Fall 2019 Enrollments')
    plt.bar(college_names, college_enrollments, color=('b','gold'))
    plt.yticks(np.arange(0, 4401, step=400))
    
    plt.xlabel('College Name')
    plt.ylabel('College Enrollment')
    
    plt.grid(False)
    plt.show()

# -------------------------------------------------

main("fall-2019.csv")
