import numpy as np # Do not import anything else
import matplotlib.pyplot as plt
units = ["CS", "ChBE", "Civil", "M&IE", "General", "CpE"] # See question 1 for a description
enrollments = [552, 563, 731, 1463, 210, 410] # See question 1 for a description
# Write the missing statements below this comment

plt.pie(enrollments,explode=(0.02,0.02,0.02,0.02,0.05,0.05),labels=units,colors=("Blue","Gold"),counterclock=False,wedgeprops = {'linewidth': 20})

plt.show()
