# WAP using recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)
a = int(input("Enter a number : "))
print(f"sum of 1st {a} numbers is {sum(a)}")