import random

def roll_dice():
    return random.randint(1,6)

print("welcome")

while True:
    input("Press enter to roll a dice...")
    print("You rolled a", roll_dice())
    play_again = input("Do you want to roll again?(y/n)").lower()

    if play_again == "n":
        break
    print("thanks for playing")

    if play_again == "y":
        input("Press enter to roll a dice...")
        print("You rolled a", roll_dice())
        play_again = input("Do you want to roll again?(y/n)").lower()
        print("press y to roll again and n to exit")
