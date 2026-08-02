# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))

# avg = (a + b + c) / 3
# print(f"Average = {avg}")

# agar inke sath sath aur 3 no. ka average nikalna ho to to ye code repeat karna padega. 

# By Functions we can avoid this repetition.
def avg():   # --> funcyion definition.
 a = int(input("Enter a number: "))
 b = int(input("Enter a number: "))
 c = int(input("Enter a number: "))

 avg = (a + b + c) / 3
 print(f"Average = {avg}")

avg()  # --> function call
avg()  
avg() 