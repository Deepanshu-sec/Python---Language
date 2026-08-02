a = int(input("Enter a number : "))
b = int(input("Enter second number : "))

if(b==0):
    raise ZeroDivisionError("Not meant to divide by Zero")
else:
    print(f"The Division is {a/b}")