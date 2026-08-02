# WAP to find out the line number of a word 'python' in a file 'log.txt' Ques 6.

with open("log.txt","r") as f:
    lines = f.readlines()

lineNo = 1 
for i in lines:
    if ("python" in i):
        print(f"Yes python is present in the file 'log.txt' at line number {lineNo} .")
        break
    lineNo += 1

else:
    print("No python is not present in the file 'log.txt' .")
