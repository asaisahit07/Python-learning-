#tuples

tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1)   
print(len(tuple1))

#sets

set1={1,"true",4,22343,3,9,6,5,7,8,10,10}
print(set1)

#addition of elements in set

set1.add(1990)
print(set1)
print(len(set1))

#removal of elements in set

set1.remove(10)
print(set1) 
print(len(set1))

#pop removes any random element from the set

set1.pop()
print(set1)
print(len(set1))

#adding tuples to set

set1.add((1,4,2,67,77))
print(set1)

#clearing the set

set1.clear()
print(set1)

#operations on sets
#union of sets and intersection of sets

set2={1,2,3,4,5,6,7,8,9}
set3={1,2,54,23,4,5,6,7,8,9}
print(set2.union(set3))              # set2 | set3 will also do union of sets
print(set2.intersection(set3))       # set2 & set3 will also do intersection of sets

#difference of sets and symmetric difference of sets

print(set2.difference(set3))            # set2 - set3 will also do difference of sets
print(set2.symmetric_difference(set3))  # set2 ^ set3 will also do symmetric 

#methods in sets
# isdisjoint() method is used to check whether two sets have any elements in common or not. If two sets have no elements in common, then it returns True, otherwise it returns False.
set4={1,2,3,4,5,6,7,8,9}
set5={10,11,12,13,14,15}
print(set4.isdisjoint(set5))  # True

#issubset() method is used to check whether all elements of a set are present in another set or not. If all elements of a set are present in another set, then it returns True, otherwise it returns False.
set6={1,2,3,4,5}
set7={1,2,3,4,5,6,7,8,9}
print(set6.issubset(set7))  # True

#issuperset() method is used to check whether a set contains all elements of another set or not. If a set contains all elements of another set, then it returns True, otherwise it returns False.
set8={1,2,3,4,5,6,7,8,9}
set9={1,2,3,4,5}
print(set8.issuperset(set9))  # True