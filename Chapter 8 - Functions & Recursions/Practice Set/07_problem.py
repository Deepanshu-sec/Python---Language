# converts inches to cm.
def inch_to_cm(inche):
     return  inche * 2.54

a = int(input("Enter inche : "))
c = inch_to_cm(a)
print(f"{round(c,2)} cm")
