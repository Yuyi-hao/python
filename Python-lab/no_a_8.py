m=int(input("Enter length: "))
n=int(input("Enter breadth: "))

def rect(m,n):
    for i in range(m):
        for j in range(n):
            print("*",end=" ")
        print()
rect(m,n)


