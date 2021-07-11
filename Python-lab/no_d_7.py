
def rand(start,end,num):
    l=[]
    for i in range(num):
        l.append(random.randint(start,end))
    return l
a=1
b=100
c=20
m=t=rand(a,b,c)
print(t)
c1=0

avg=sum(t)/c
print("average: ",avg)
print("largest: ",max(t))
print("smallest: ",min(t))

t.sort()
t.pop()
print("2nd largest: ",max(t))
print("2nd smallest: ",t[1])

for i in m:
   if(i%2==0):
       c1=c1+1
print("total even no: ",c1)
