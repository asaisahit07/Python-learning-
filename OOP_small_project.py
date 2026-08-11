#this program is to just test the OOP concepts in python.


class Student:
    def __init__(self,name,age,branch,marks):
        self.name=name
        self.age=age
        self.branch=branch
        self.marks=marks
    def display(self):
        print("Name : ",self.name)
        print("AGE : ",self.age)
        print("Branch : ",self.branch)
        print("Makrs :",self.marks)
student1=Student("roshan","20","IT",90)
student1.display()
print("\n")
student2=Student("shyam","21","CS",80)
student2.display()
print("\n")  
student3=Student("shait","22","IT",70)  
student3.display()
