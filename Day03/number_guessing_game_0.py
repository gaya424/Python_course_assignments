import random

def main():
    # The computer "thinks" of a random number between 1 and 20
    number = random.randint(1, 20)
    
    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 20: "))
    
    # Check the user's guess
    if guess < number:
        print("Your guess is smaller than the number.")
    elif guess > number:
        print("Your guess is bigger than the number.")
    else:
        print("Congratulations! You guessed the number.")

if __name__ == "__main__":
    main()