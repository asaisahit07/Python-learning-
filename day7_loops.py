#for loops

i=[1,2,3,4,5,6]
for x in i:
    print(x)

names=['sahit','sahil','sahith','sahithi']
for name in names:
    print(name)

names='sahit'        
for name in names:
    print(name)
print("\n")
#for else loop


i=[1,2,3,4,5,6]
for x in i:
    print(x)
else:
    print("the loop is completed")

print("\n")

names=['sahit','sahil','sahith','sahithi']
for name in names:
    print(name)
    if(name=='sahith'):
        print("similar name found")
        break
else:
    print("the loop is completed")        

print("\n")
#average height of students
height=input("enter the heights of students separated by space = ").split()
total_height=0
for h in height:
    total_height+=int(h)
total_students=len(height)
average_height=total_height/total_students
print("the average height of the students is ", average_height)
print("\n")


#find maximum number in a list

number=input("enter the number separated by space = ").split()
max_number=0
for n in number:
    if(int(n)>max_number):
        max_number=int(n) 
print("the maximum number in the list is ", max_number)
print("\n")


#range
#range(start,stop,step)
sum=0
for i in range(0,101,2):
    sum+=i
print("the sum of even numbers from 0 to 100 is ", sum)    


#print buzz if the number is divisible by 3 print fizz if the number is divisible by 5 print buzz if the number is divisible by both 3 and 5 print fizzbuzz
for i in range(0,101):
    if(i%3==0 and i%5==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("buzz")
    elif(i%5==0):
        print("fizz")    
    else:
        print(i)

        