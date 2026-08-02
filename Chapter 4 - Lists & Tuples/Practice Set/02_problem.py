# WAP to accept marks of 6 student and display them in a sorted manner. 
# WAP to store seven marks in a list entered by the user.
marks = []
f1 = int(input("Enter marks 1 name : "))
marks.append(f1)
f2 = int(input("Enter marks 2 name : "))
marks.append(f2)
f3 = int(input("Enter marks 3 name : "))
marks.append(f3)
f4 = int(input("Enter marks 4 name : "))
marks.append(f4)
f5 = int(input("Enter marks 5 name : "))
marks.append(f5)
f6 = int(input("Enter marks 6 name : "))
marks.append(f6)


print("Markes are : ",  sorted(marks))

