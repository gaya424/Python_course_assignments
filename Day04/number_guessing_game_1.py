import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Guess the number between 1 and 20.")

while True:
    user_input = input("Enter your guess: ").strip()

    guess = int(user_input)
    if guess < secret_number:
            print("Your guess is smaller than the number.")
    elif guess > secret_number:
            print("Your guess is bigger than the number.")
    else:
            print("Congratulations! You guessed the number.")
            break
