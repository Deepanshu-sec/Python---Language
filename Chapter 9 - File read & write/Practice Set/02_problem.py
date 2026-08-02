# The game() function in a program lets a user play a game and returns the score as an integer.
# Yoy need to read a file 'Hi-score.txt' which is either empty or contains the previous Hi-score.
# You need to write a program to update the Hi-score wehenever the game() function breaks the 
# Hi-score.
import random
def game():
    print("You are playing the game : ")
    score = random.randint(1,100)
    with open("hiscore.txt") as f:
           data = f.read()
           if(data!=""):
                 data = int(data)
           else:
                 data = 0
    print(f"your High score is {score}")
    if(score>data):
          with open("hiscore.txt","w") as f:
                f.write(str(score))
          return score

game()



  