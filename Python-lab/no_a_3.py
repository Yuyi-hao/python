n=int(input("Enter a no :  "))

if(n%2==0):
    print("even")
else:
    print("Odd")

# using bit wise operator 
res = ""
if(n & 1):
    res = 'odd'
else:
    res = 'even'

print(f"{n} is an {res} number")