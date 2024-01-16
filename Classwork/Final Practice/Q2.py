import numpy as np
# -------------------------------
class Course:
    def __init__(self, rubric, number):
        self.rubric = rubric
        self.number = number
    def __str__(self):
        return self.rubric + " " + str(self.number)
# -------------------------------
def main():
    my_courses = Course_Schedule(3)
    course_1 = Course("CSCI", 127)
    my_courses.add(course_1)
    course_2 = Course("M", 171)
    my_courses.add(course_2)
    course_3 = Course("WRIT", 101)
    my_courses.add(course_3)
    print(my_courses)
# -------------------------------
main()
        
        
