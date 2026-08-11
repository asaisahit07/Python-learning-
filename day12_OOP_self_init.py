

# OOP - Self and Init

class instructor:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Instructor name is:",self.name)
        print("Instructor age is:",self.age)
instructor1=instructor("Roshan",20)
instructor2=instructor("Shyam",21)
print("\n")

#class methods 

class instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(self.name)
        print(self.address)
instructor1=instructor("Roshan","Kathmandu")
instructor1.display()