# WAP to find the greatest of four numbers entered by the user.
a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
c = int(input("Enter the number 3 : "))
d = int(input("Enter the number 4 : "))

if(a>b and a>c and a>d):
    print("Greatest Number is a : ",a)
elif(b>a and b>c and b>d):
    print("Greatest Number is b : ",b)
elif(c>a and c>b and c>d):
    print("Greatest Number is c : ",c)
else:
    print("Greatest Number is d : ",d)