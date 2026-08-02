# WAP to calculate the factorial of given number using for loop.
n = int(input("Enter a number : "))

fact = 1
for i in range(1,n+1):
    fact = fact * i

print(f"The Factorial of {n} is = {fact}")
