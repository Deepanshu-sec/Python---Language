# WAP to find out whether a given post is talking about "Deepanshu" or not.
post = input("Enter the post : ")

if("Deepanshu".lower() in post.lower()):
    print("This post is talking about Deepanshu: ")

else:
    print("This post is not talking about Deepanshu: ")