# WAP to find out whether a file is identical & matches the content of another file.

with open("donkey.txt","r") as f:
    data = f.read()

with open("poems.txt","r") as f:
    data1 = f.read()

if(data==data1):
    print("Both files are identical.")
else:
    print("Both files are not identical.")
