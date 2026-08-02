#this program is totally built on CRUD(create,read,update,delete) principles
#this program is to develop a menu driven python application that stores and manages student records using dictionary data

print("---------WELCOME TO GMRIT PORTAL-----------")
student_record={}
def add_student():
    student_id=int(input("enter the student id = "))
    name=input("enter the student name = ")
    age=int(input("enter the student age = "))
    branch=input("enter the student branch = ")
    python=int(input("enter the student python marks = "))
    java=int(input("enter the student java marks = "))
    DBMS=int(input("enter the student DBMS marks = "))
    student_record[student_id]={'name':name,'age':age,'branch':branch,'marks':{'python':python,'java':java,'DBMS':DBMS}}


def search_student():
    student_id=int(input("enter the student id = "))
    if student_id in student_record:
        print("student details are = ",student_record[student_id])
    else:
        print("student id not found")

def update_student():
    student_id=int(input("enter the student id = "))
    if student_id in student_record:
        while True:
            print("1. update name")
            print("2. update age")
            print("3. update branch")
            print("4. update marks")
            print("5.exit")
            update_choice=int(input("enter your choice = "))
            if update_choice==1:
                name=input("enter the new name = ")
                student_record[student_id]['name']=name
            elif update_choice==2:
                age=int(input("enter the new age = "))
                student_record[student_id]['age']=age
            elif update_choice==3:
                branch=input("enter the new branch = ")
                student_record[student_id]['branch']=branch
            elif update_choice==4:
                while True:
                    print("1. update python marks")
                    print("2. update java marks")
                    print("3. update DBMS marks")
                    print("4. exit")
                    marks_choice=int(input("enter your choice = "))
                    if marks_choice==1:
                        python=int(input("enter the new python marks = "))
                        student_record[student_id]['marks']['python']=python
                    elif marks_choice==2:
                        java=int(input("enter the new java marks = "))
                        student_record[student_id]['marks']['java']=java
                    elif marks_choice==3:
                        DBMS=int(input("enter the new DBMS marks = "))
                        student_record[student_id]['marks']['DBMS']=DBMS
                    elif marks_choice==4:
                        break
                    else:
                        print("invalid choice")
            elif update_choice==5:
                break
            else:
                print("invalid choice")
    else:
        print("student id not found")


def delete_student():
    student_id=int(input("enter the student id = "))
    if student_id in student_record:
        del student_record[student_id]
        print("student record deleted successfully")
    else:
        print("student id not found")

def display_student():
    student_id=int(input("enter the student id = "))
    if student_id in student_record:
        print("the student details are = ",student_record[student_id])
    else:
        print("student id not found")

def display_all_students():
    if len(student_record)==0:
        print("no students records found")
    else:
        for i in student_record:
            print("student id = ",i)
            print("student details are = ",student_record[i])

print("---------WELCOME TO STUDENT RECORD MANAGEMENT SYSTEM-----------")
print("\n")
print("---------MENU-----------")
print("\n")
while True:
    print("1. add student record")
    print("2. search student record")
    print("3. update student record")
    print("4. delete student record")
    print("5. display student records")
    print("6. display all student records")
    print("7. exit")
    choice=int(input("enter your choice = "))
    if choice==1:
        add_student()
    elif choice==2:
        search_student()        
    elif choice==3:
        update_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        display_student()
    elif choice==6:
        display_all_students()
    elif choice==7:
        print("thank you for using the student record management system")
        break   
