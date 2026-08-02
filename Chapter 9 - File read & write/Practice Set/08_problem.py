# WAP to make a copy of a text file 'poems.txt'.
with open("poems.txt","r") as f:
      data = f.read()

with open("poems_copy.txt","w") as f:
      f.write(data)

