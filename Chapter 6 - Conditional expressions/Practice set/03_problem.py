# WAP to find out whether a student has passed or failed if it requires a total of 40% and 
# atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
a = int(input("Enter marks 1 : "))
b = int(input("Enter marks 2 : "))
c = int(input("Enter marks 3 : "))

total_percentage = (a + b + c)/300 * 100

if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print("PASSED 🦇",total_percentage)
else:
    print("FAILED 🙂",total_percentage)