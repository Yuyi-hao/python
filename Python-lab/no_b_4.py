a=0
b=1
c=0
s=0

while(c<4000):
    print(c)
    c=a+b
    a=b
    b=c
    if(c%2==0):
        s+=c
  
    
print(s)  
    
