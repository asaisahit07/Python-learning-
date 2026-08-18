#this is about the inheritance and its types in python

# we dont use extend keyword in python for inherting the properties of the parent class to child class
#instead we use the name of the parent class beside the name of the child class definiton inside the parenthesis

class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class child(parent):
    def det(self):
        print("the child parent name is : ",self.name)
        print("the child parent age is : ",self.age)
obj=child('sahit',55)
obj.det()
print("\n")

# if we want to access the properties of the parent class in child class we can use super keyword


# single inheritance
class HUMAN:
    def eat(self):
        print("I can eat")
    def work(self):
        print(" i can work")
class MALE(HUMAN):
    def flirt(self):
        print("i can flirt")
    def work(self):                 #this is called method overriding where we use the same method name but different parameters
        super().work()              #this is the use of super keyword to access the properties from the parent class while having the overriding
        print("i can code")
male_1=MALE()
male_1.flirt()
male_1.eat()
male_1.work()
print("\n")


# multiple inheritance 

class Human:
    def eat(self):
        print("i can eat")
class being:
    def code(self):
        print("i can code")
class child(Human,being):
    def details(self):
        print(" i can work too")
obj=child()
obj.details()
obj.code()
obj.eat()