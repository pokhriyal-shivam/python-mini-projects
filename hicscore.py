import random

def game():
    print("You are playing a game...")
    score = random.randint(1, 60)

    # Read high score safely
    try:
        with open("hiscore.txt") as f:
            hiscore = f.read()
            if hiscore != "":
                hiscore = int(hiscore)
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score is: {score}")

    # Update high score if needed
    if score > hiscore:
        print("New High Score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
