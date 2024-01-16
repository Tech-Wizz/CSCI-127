import pandas as pd # Do not import anything else

units = ["Chemical and Biological Engineering", "Civil Engineering", "Computer Engineering", "General Engineering","Mechanical and Industrial Engineering","School of Computing"]
enrollments = [563, 731, 410, 210, 1463, 552] # 563 students in Chemical and Biological Engineering, etc.
dataset = list(zip(units, enrollments))
dataframe = pd.DataFrame(data=dataset, columns=["Unit", "Enrollment"])
# Write the missing statements below this comment
