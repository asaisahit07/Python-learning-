# This program stores student details and prints the final result of the student


print("---------WELCOME TO GMRIT PORTAL-----------")

name = input("Enter your name : ")
roll_number = int(input("Enter your respective roll number : "))
branch = input("Enter the branch : ")
semester = int(input("Enter your current semester : "))

sub = int(input("Enter no. of subjects : "))

count = 0
subject = []
marks = []


# Taking subject details
while count < sub:

    subject_name = input("Enter the name of the subject : ")
    subject.append(subject_name)

    subject_marks = int(input("Enter the marks in the subject : "))
    marks.append(subject_marks)

    count += 1



# Function to calculate total marks
def total_marks():

    total_mark = 0

    for i in marks:
        total_mark += i

    return total_mark



# Function to find highest marks
def highest_mark():

    highest = max(marks)

    return highest



# Function to find lowest marks
def lowest_marks():

    lowest = min(marks)

    return lowest



# Function to calculate percentage
def percentage():

    total = total_marks()

    maximum_marks = sub * 100

    percent = (total / maximum_marks) * 100

    return percent



# Function to calculate grade
def grades():

    percent = percentage()

    if percent >= 90:
        return "S"

    elif percent >= 80:
        return "A+"

    elif percent >= 70:
        return "A"

    elif percent >= 60:
        return "B"

    elif percent >= 50:
        return "C"

    else:
        return "FAIL"



# Function to check failed subjects
def subject_fail():

    for i in marks:

        if i < 35:
            return "Student has failed in a subject"

    return "Student passed all subjects"



# Function to check scholarship eligibility
def scholarship():

    percent = percentage()

    if percent >= 85:
        return "Eligible for Scholarship"

    else:
        return "Not Eligible for Scholarship"



# Storing results
total = total_marks()
highest = highest_mark()
lowest = lowest_marks()
percent = percentage()
grade = grades()
fail_status = subject_fail()
scholarship_status = scholarship()



# Final Result Report

print("\n--------- FINAL RESULT ---------")

print("NAME :", name)
print("ROLL NO :", roll_number)
print("BRANCH :", branch.upper())
print("SEMESTER :", semester)

print("\nSUBJECT DETAILS")

for i in range(sub):
    print(subject[i], ":", marks[i])


print("\n------------------------------")

print("TOTAL MARKS :", total)
print("PERCENTAGE :", percent, "%")
print("HIGHEST MARK :", highest)
print("LOWEST MARK :", lowest)
print("GRADE :", grade)

print(fail_status)

print("SCHOLARSHIP STATUS :", scholarship_status)

print("------------------------------")
print("THANK YOU FOR CHOOSING GMRIT")