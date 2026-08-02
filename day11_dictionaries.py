#dict_name={key:value}
phone_no={'sahit':1234,'roshan':3444}
print(phone_no)
print("\n")

#or can be written like this too

phone_num={'sahit':1234,
           'shyam':3424,
           'roshan':3342}
print(phone_num)
print(phone_num['roshan'])
print("\n")

#or we simply use dict function 

phone_num=dict(roshan=3424,shait=1234,shyam=4433)
print(phone_num)
print("\n")

#updation of the key values

phone_num['roshan']=9509694
print(phone_num)
print("\n")

#adding ne wkey value

phone_num['madhav']=1234
print(phone_num)
phone_num['ritwik']={1233,3234,4455}     #we can also add a set as a value to a key
print(phone_num)
print("\n")

#if you want to add two names to a single ey value
phone_num['sahit']={'sahit_home':334422,'sahit_office':445533}
print(phone_num)
print("\n")
print(phone_num.get('roshan')) #this will return the value of the key
print("\n")

#deletion of key value pair
del phone_num['sahit']
print(phone_num)
print("\n")

#or we can use pop
phone_num.pop('roshan')
print(phone_num)
print("\n")

#popitem will delete the last key vlaue
phone_num.popitem()
print(phone_num)
print("\n")

#clear will remove all teh keys
phone_no.clear()
print(phone_no)
print("\n")

for i in phone_num.items():
    print(i)
print("\n")    

#nested dictionaries
student_data={
    'ram':{'roll_no':123,'age':20},
    'sahit':{'roll_no':123,'age':20}
}
print(student_data)
print(student_data['ram'])
print(student_data['sahit']['roll_no'])