# Mini Project 1
# BMI Calculator
# Built using Python Basics + Operators

Weight=input("enter hte weight in kg =")
Weight=int(Weight)
height=input("enter the height in meters =")
height=float(height)
BMI=Weight/(height**2)
print("your designated BMI is =",int(BMI))
 
 #by using int(BMI) we are converting the float value of BMI into integer value to get the whole number of BMI and not the decimal value of BMI 