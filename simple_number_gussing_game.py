import random

try:
    _wel = "welcome to number guessing game"
    _wel.capitalize()
    print(_wel)
    computer = random.randint(1,10)
    
    while(True):

        player = int(input("enter your number :- "))

        if player > computer:
            print("you guess worng number (-_-)\n piz....try again")
            print("i am thinking smaller number")

        elif player < computer :
            print("you guess worng number (-_-)\n piz....try again")
            print("i am thinking bigger number")
            
        elif player == computer :
            print("cango ('~')\n you win the game")
            break
        
except Exception as ex :
    print(ex)
    print("author :- shubham mane mail ID - maneshubham4033@gamil.com")

finally:
    print(" ")             
    