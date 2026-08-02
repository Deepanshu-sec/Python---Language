a = 19

def func():
    global a  # --> Change the value of global variable
    a = 3
    print(a)

func()      # --> 1
print(a)    # --> 2