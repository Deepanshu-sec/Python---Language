# WAP to display a/b where a and b are integers. if b=0, display infinite by handling the 
# 'ZeroDivisionError' .

try:
    a = int(input("Enter a number : "))
    b = int(input("Enter b number : "))
    print(a/b)

except ZeroDivisionError as e:
    print("Infinite")