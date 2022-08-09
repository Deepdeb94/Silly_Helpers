
no_of_student = int(input('No of students: '))
students = []
for _ in range(no_of_student):
    student = input('Student name: ')
    students += [student]
    
for i in range(len(students)):
    print(i + 1, students[i])