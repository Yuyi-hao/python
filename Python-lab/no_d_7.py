
from random import randint
def rand(start,end,num):
    l=[]
    for i in range(num):
        l.append(randint(start,end))
    return l

a, b, c=1, 100, 20
t=rand(a,b,c)  # [randint(start,end) for _ in range(c)] one liner
print(*[i for i in t]) # will print without '[]'
c1=0

avg=sum(t)/c
print(f"Average: {avg}")
print(f"Largest: {max(t)}")
print(f"Smallest: {min(t)}")

t.sort()
print(f"2nd largest: {t[-2]}") # second largest could be found with t[-1] after sorting
print(f"2nd smallest: {t[1]}")

for i in t:
   if(i%2==0):
       c1=c1+1
print(f"Total even number: {c1}")
