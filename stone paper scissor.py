# a stone paper scissor game using python
import random
'''
stone = 1

paper = -1

scissor = 0

'''

computer = random.choice([1,-1,0])
user = input("enter your choice from stone , paper , scissor:")
yourdict = {"stone": 1 ,"paper": -1,"scissor": 0}
reversedict = {1:"stone",-1:"paper",0:"scissor"}

you = yourdict[user]

print (f"you chose {reversedict[you]}\n computer chose {reversedict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == 1 and you == -1):
        print("you win!!")

    elif(computer == 1 and you == 0):
        print("you lose!!")

    elif(computer == -1 and you == 1):
        print("you lose!!")

    elif(computer == -1 and you == 0):
        print("you win!!")

    elif(computer == 0 and you == -1):
        print("you lose!!")

    elif(computer == 0 and you == 1):
        print("you win!!")

    else:
        print("something went wrong")
