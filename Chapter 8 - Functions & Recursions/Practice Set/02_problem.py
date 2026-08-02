# WAP using function to find the greatest of 3 numbers.

def greatest(a,b,c):
     if(a>b and a>c):
          print(f" a is the greatest number.")
     elif(b>a and b>c):
          print(f" b is the greatest number.")
     else:
            print(f" c is the greatest number.")

a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))
c = int(input("Enter a number c : "))

greatest(a,b,c)