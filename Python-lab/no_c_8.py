n=int(input("Enter no: "))
def sum_digit(n):
    s=0
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    if s<10:
        print(s)
    else:
        sum_digit(s)
sum_digit(n)
