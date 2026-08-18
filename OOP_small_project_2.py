# this program is just te=he implementation of the concepts i learned till day13

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("NAME : ",self.name)
        print("AGE : ",self.age)


class college:
    def __init__(self,clg_name):
        self.clg_name=clg_name

    def display_details(self):
        print("COLLEGE NAME : ",self.clg_name)


class student(person,college):
    def __init__(self,name,age,clg_name,branch,marks):
        person.__init__(self,name,age)
        college.__init__(self,clg_name)
        self.branch=branch
        self.marks=marks
    def display_student(self):
        print("BRANCH : ",self.branch)
        print("MARKS : ",self.marks)

details=student('sahit',19,'GMRIT','IT',9.25)
print("-----STUDENT DETAILS----")
details.display_person()
details.display_details()
details.display_student()