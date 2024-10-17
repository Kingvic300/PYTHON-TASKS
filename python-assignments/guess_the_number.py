import random

def game():
    number_to_guess = random.randint(1, 1000)
    number_of_trials = 0
    pass_status = False

    while pass_status == False:
        guess = int(input("Guess a number between 1 and 1000: "))
        number_of_trials += 1

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            pass_status = True

    print("Correct! You got the answer. Stay tuned for your reward.")
    print(f"You guessed {number_of_trials} times.")

    play_again = input("Do you want to play again, Enter 1 to play again and 0 to quit: ")
    number = int(play_again)

    if number == 1:
        game()
    else:
        print("Thanks for playing")

game()


