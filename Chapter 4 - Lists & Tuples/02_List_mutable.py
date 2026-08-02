# Concept of list's Mutablity. 

friend = ["Harvey", 8 , 0.95 , "Deepanshu", True]
print(friend)

# Methods return The original list, unlike strings. 
friend.append("Mike Ross")      # --> (append) add Something in list's end.
print(friend)

# Now friend[5] is in the original list.
print(friend[4])
print(friend[5])