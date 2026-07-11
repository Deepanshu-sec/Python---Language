# --> Specifies the type of a .
a = 6
t = type(a)  
print(t)

# --> Change the type of x from float to integer.
x = 698.45
t = int(x)    
print(t)

# --> changes the type of b from string to float.
b = "6.0"
t = float(b) 
print(t)

# --> print same float value bcz we can't convert float to string.
c = 7.0
t = str(c)  
print(t)

# --> This will give an error because we cannot convert a string to an integer.
# d = "Deepanshu"
# t = int(d)
# print(t)    