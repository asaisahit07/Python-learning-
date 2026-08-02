print("----WELCOME----")
student_marks={'sahit':98,'roshan':99,'ritwik':100,'shyam':34,'madhav':45}
print(student_marks)
print("\n")
student_grades={}
for i in student_marks:
    marks=student_marks[i]
    if marks>90:
        student_grades[i]="A+"
    elif marks>80:
        student_grades[i]="A"
    elif marks>70:
        student_grades[i]="B+"
    elif marks>60:
        student_grades[i]="B"
    elif marks>50:
        student_grades[i]="C"
    elif marks>40:
        student_grades[i]="D"
    else:
        student_grades[i]="F"
print(student_grades)
print("\n")