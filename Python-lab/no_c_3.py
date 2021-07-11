a=input("Enter any character: ")

a=ord(a)

if(a>=65 and a<=90):
    print("uppercase alphabet")
elif (a>=97 and a<=122):
    print("lowercase alphabet")
elif (a>=48 and a<=57):
    print("digit")
else:
    print("special symbol")
