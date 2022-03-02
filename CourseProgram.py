"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

import CourseClass as c


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    my_course = c.Course(name, seats, status, students)
    seats = 4

    for student in students:
        newstudent = c.Register(student, crn)
        if seats != 0:
            seats -= 1
            print("Student Name:", newstudent.get_name())
            print("Course Name:", my_course.get_name())
            print("Seats left:", seats)
        else:
            print(
                "Sorry ",
                newstudent.get_name(),
                ", registration is closed for ",
                my_course.get_name(),
            )


main()

# it clicked at the last second - i wasted sm time UGH
