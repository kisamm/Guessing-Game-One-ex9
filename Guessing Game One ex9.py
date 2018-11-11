import random

score = 0

keep_playing = True
while keep_playing:
    user = int(input("Choose a number beetween 1-9 "))
    numbers = int(random.randint(1,9))
    print("Computer choose", numbers)
    print("Your number is", user)

    if numbers == user:
        print("Nice! You guessed")
        score = score +1
    elif numbers < user:
        print("Too high")
        score = score -1
    elif numbers > user:
        print("Too low")
        score -=1

    new_choice = input("Do you wanna play again? y/n")
    if new_choice == "y":
        keep_playing = True
    elif new_choice == "n":
        keep_playing = False
        print("Your score on the end is ", score)








