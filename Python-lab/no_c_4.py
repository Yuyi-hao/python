num1=int(input("enter 1st no: "))
num2=int(input("enter 2nd no: "))

i=1

while(i<num1+1):
    if((num1%i==0) and (num2%i==0)):
        g=i
    i+=1
print(g)
