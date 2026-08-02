# WAP to mine a log file and find our whether it contains 'python'.
with open("log.txt","r") as f:
      data = f.read()

if ("python" in data):
      print("Yes python is present in the file 'log.txt' .")

else:
      print("No python is not present in the file 'log.txt' .")