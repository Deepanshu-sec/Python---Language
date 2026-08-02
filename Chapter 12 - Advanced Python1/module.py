def myFunc():
    print("Hello Deepanshu")

if __name__ == "__main__":      # main file me ye chalega 
    print("we are directly running this code")
    myFunc()
    print(__name__)

else:                       # Imported code file me ye chalega 
    myFunc()
    print(__name__)