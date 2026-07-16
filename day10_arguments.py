#arguments

def greet(name,dpt):
    print(f"hi {name}")
    print(f"are from {dpt} department?")
greet("sahit","IT")
print("\n") 

#using tuple
# *arg and **kwargs
def add(*number):
    c=0
    for i in number:
        c+=i
    print(f"the sum is {c}")
add(9,6,7)    
add(5,4,3,21)
print("\n")

def add(*num,name):
    c=0
    print(num)
    print(name)
    for i in num:
        c+=i
    print(f"the sum is {c}")
add(9,6,name="sahit")    
add(5,4,3,name="roshan")
print("\n")

#kwargs

def info_person(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
info_person(name="sahit",age="19",branch="IT")
info_person(name="roshan",age="19",branch="ECE") 
print("\n")

# *args and **kwargs combined 

def info_person(*args,**kwargs):
    for i,j in kwargs.items():
        print(i,j)
    print(args)  
info_person(1,2,3,name="sahit")
info_person(4,5,6,name="roshan")
print("\n")      