import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
debug_mode = False

print("Guess the number between 1 and 20.")
print("Type 'x' to exit, 's' to show the secret number (cheat), or 'd' to toggle debug mode.")

while True:
    if debug_mode:
        print(f"[DEBUG] Current secret number: {secret_number}")
    
    user_input = input("Enter your guess: ").strip()

    if user_input.lower() == 'x':
        print("You exited the game.")
        break

    elif user_input.lower() == 's':
        print(f"The secret number is: {secret_number}")
        continue

    elif user_input.lower() == 'd':
        debug_mode = not debug_mode
        print(f"Debug mode {'enabled' if debug_mode else 'disabled'}.")
        continue

    elif user_input.isdigit():
        guess = int(user_input)
        if guess < secret_number:
            print("Your guess is smaller than the number.")
        elif guess > secret_number:
            print("Your guess is bigger than the number.")
        else:
            print("Congratulations! You guessed the number.")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 20, or 'x', 's', or 'd'.")
