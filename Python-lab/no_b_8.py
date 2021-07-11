def sum_digit(n):
    s=0
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    return s
print(sum_digit(2336))
