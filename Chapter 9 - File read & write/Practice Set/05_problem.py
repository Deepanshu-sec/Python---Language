# repeat program 4 for a list of such words to be censored.
words = ["donkey","stupid","idiot"]

with open("donkey.txt","r") as f:
    data = f.read()

for i in words:
    data = data.replace(i,"#"*len(i))   # "#" * len(i) --> word ki len() k according # honge.

with open("donkey.txt","w") as f:
    f.write(data)