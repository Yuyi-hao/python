import math as m

x1=int(input("Enter 1st point of x axis: "))
x2=int(input("Enter 2nd point of x axis: "))
y1=int(input("Enter 1st point of y axis: "))
y2=int(input("Enter 1st point of y axis: "))

distance=m.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(distance)


#or
d=m.sqrt(m.pow(x2-x1,2)+m.pow(y2-y1,2))
print(d)
