#this program can be used to estimate the amount of paint used to paint the wall 

print("----no.of cans of paint needed----")
h=int(input("enter the height of the wall = "))
w=int(input("enter the width of the wall = "))
cover=7         #this shows that one can is able to cover 7 sq.c  

def paint_coverage(height,width,coverage):
    height=h
    width=w
    coverage=cover
    area=(height*width)
    cans=round((area/coverage),2)
    print(f"you need {cans} cans to paint the wall")
paint_coverage(height=h,width=w,coverage=cover)    