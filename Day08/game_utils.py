import random

def generate_secret_number():
    return random.randint(1, 20)

def toggle_flag(flag):
    return not flag

def shift_number(secret_number):
    shift = random.choice([-2, -1, 0, 1, 2])
    new_number = secret_number + shift
    new_number = max(1, min(new_number, 20))
    return new_number, shift

def process_guess(guess, secret_number):
    if guess < secret_number:
        return "Your guess is smaller than the number.", False
    elif guess > secret_number:
        return "Your guess is bigger than the number.", False
    else:
        return "Congratulations! You guessed the number.", True

def is_valid_number(input_str):
    return input_str.isdigit()
