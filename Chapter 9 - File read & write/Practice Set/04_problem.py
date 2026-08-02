# A file contains a word 'donkey multiple times. You need to write a program which replaces this 
# word with '#####' by updating the file.

with open("donkey.txt","r") as f:
       data = f.read()

data = data.replace("donkey","######") 

with open("donkey.txt","w") as f:
       f.write(data)