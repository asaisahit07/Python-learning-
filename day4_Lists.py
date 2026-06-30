#lists   
roll_no=[1000,4,35,"sahit",5,61,7,18,92,120]
print(roll_no) 
print(roll_no[3])
print(len(roll_no))
print(roll_no[2:4])

#sorting of list
number=[100,23,1,43,2,67,78,54,23,90,43,52,45,61,12,34,56,78,90]
number.sort()
print(number)

#reverse  of list
number.reverse()
print(number)
print(max(number))  

#append() is used to add an element at the end of the list
integers=[1,2,3,4,5,6,7,8,9,0,12,13]
integers.append(23)
integers.append(24)
print(integers)

#insert() is used to add an element at a specific index of the list
op=[1,2,3,4,5,6,7,8,9]
op.insert(3,45)
op.insert(6,46)
print(op)

#extend() is used to insert more than 1 element at a time at the end of the list
oi=[1,2,3,4,5,6,7,8,9]
oi.extend([23,24,25,26,27])
print(oi)

#remove() is used to delete a element from the list
on=[1,2,3,4,5,6,7,8,9]
on.remove(3)
print(on)

#pop() s used to remove the last element
ou=[1,2,3,4,5,6,7,8,9]
ou.pop(4)
print(ou)
