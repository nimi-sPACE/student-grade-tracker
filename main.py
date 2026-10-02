#Should collect Student ID, Name, Department, and Level and store them as student information.

name = input('Enter Student Name: ')
department =input('Enter Department: ')
student_id = input('Enter Student ID: ')
level = int(input('Enter level: '))


student = {
    "Name": name, 
    "Department": department,
    "Student ID": student_id,
    "Level": level
}

print("Student Information")
for key, value in student.items():
    print(f"{key}: {value}")
