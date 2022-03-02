"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

from unicodedata import name
import CourseClass as c


def main():

    # name = 'MIS 4322 - Advanced Python'
    # crn = '250309'
    # seats = 4
    # status = 'open'
    # students = ['John','James','Jill','Jack','Joanne']

    my_course = c.Course("MIS 4322 - Advanced Python", "250309", 4, "open")

    my_student1 = c.Register("John", "250309")
    my_student2 = c.Register("James", "250309")
    my_student3 = c.Register("Jill", "250309")
    my_student4 = c.Register("Jack", "250309")

    print("Student Name:", my_student1.get_student_name())
    print("Course Name:", my_student1.get_name())
    print("CRN:", my_student1.get_crn())
    print("Seats left:", my_student1.get_seats())
    print()

    print()
    print("Student Name:", my_student2.get_studentname())
    print("Course Name:", my_student2.get_name())
    print("CRN:", my_student2.get_crn())
    print("Seats left:", my_student2.get_seats())
    print()

    print()
    print("Student Name:", my_student3.get_studentname())
    print("Course Name:", my_student3.get_name())
    print("CRN:", my_student3.get_crn())
    print("Seats left:", my_student3.get_seats())
    print()

    print()
    print("Student Name:", my_student4.get_studentname())
    print("Course Name:", my_student4.get_name())
    print("CRN:", my_student4.get_crn())
    print("Seats left:", my_student4.get_seats())
    print()

    if my_student1.get_crn() == my_course.get_crn():
        seat_count -= my_course.__seats()

    if my_student2.get_crn() == my_course.get_crn():
        seat_count -= my_course.__seats()

    if my_student3.get_crn() == my_course.get_crn():
        seat_count -= my_course.__seats()

    if my_student4.get_crn() == my_course.get_crn():
        seat_count -= my_course.__seats()

    if my_course.get_status() == "closed":
        print("Sorry ", name, ", registration is closed for MIS 4322 - Advanced Python")


main()
