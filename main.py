#Should collect Student ID, Name, Department, and Level and store them as student information.

name = input('Enter Student Name: ')
department =input('Enter Department: ')
student_id = input('Enter Student ID: ')
level = int(input('Enter level: '))


student = {
    "Name": name, 
    "Department": department,
    "Student ID": student_id,
    "Level": level,
    "Courses": [],
}


    #Add courses to the student information. The user should be able to add multiple courses.

course = input('Enter course:').replace(" ", "").upper()
student["Courses"].append(course)


while True:
    more_courses = input('Do you want to add more courses? (yes/no): ').strip().lower()
    if more_courses.lower() == 'yes':
        course = input('Enter course:').replace(" ", "").upper()

        if course not in student["Courses"]:
            student["Courses"].append(course)
        else:
            print("This course has already been added.")
        
    elif more_courses.lower() == 'no':
        break

    else:
        print('Please enter (yes/no)')
        
        

print("Student Information")
for key, value in student.items():
    if key != "Courses":
      print(f"{key}: {value}")

#Display the student courses.
print("Courses:")
for course in student["Courses"]:
    print(f" -  {course}")





