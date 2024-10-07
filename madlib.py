import random

secret_number = random.randint(1, 10)
guess = int(input("Guess the secret_number: "))
print(secret_number)

match guess:
    case 1 | 10:
        if guess > secret_number:
            print(f"{guess} is too high. Try again??")
            play_again = input("input yes or no: ")
            if play_again == "yes":
                 guess = int(input("Guess the secret_number: "))

        elif guess < secret_number:
            print(f"{guess} is low. Try again??.")
        else:
            print("Congratulations, you guessed it right.")
    case _:
        print(f"{guess} not an integer")
