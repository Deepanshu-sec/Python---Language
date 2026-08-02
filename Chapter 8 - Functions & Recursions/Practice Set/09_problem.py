# Write a function to print multiplication table of a given no.
def mult(n):
    for i in range(1,11):
        print(f"{n} * {i} = {i*n}")

a = int(input("Enter a number : "))
mult(a)