sandwiches = [0,1,0,1]
students = [1,1,0,0]

while sandwiches and students and sandwiches[0] in students:
    if sandwiches[0] == students[0]:
        students.pop(0)
        sandwiches.pop(0)
    else:
        students.append(students[0])
        students.pop(0)
    print(students)
