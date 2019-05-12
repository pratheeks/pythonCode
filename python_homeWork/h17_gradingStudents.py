def gradingStudents(grades):
    for i in grades:
        if i<38:
            print(i)
        else:
            x=i//5
            y=(x*5)+5
            if y-i<3:
                print(y)
            else:
                print(i)

n = 4

grades = [73,67,38,33]

#for _ in range(n):
#    grades_item = int(input())
#    grades.append(grades_item)

result = gradingStudents(grades)
