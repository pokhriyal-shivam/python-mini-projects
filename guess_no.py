import random

n = random.randint(1,100)
userno = -1
guess = 0
while(userno != n):
    guess += 1
    userno = int(input("guess the no between 1 and 100 :"))
    if(userno>n):
        print("lower the number")
    else:
        print("higher the number")

print(f"you guessed the number {n} in {guess} guesses")
