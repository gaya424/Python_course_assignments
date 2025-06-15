from game_utils import (
    generate_secret_number,
    toggle_flag,
    shift_number,
    process_guess,
    is_valid_number
)

def main():
    secret_number = generate_secret_number()
    debug_mode = False
    move_mode = False

    print("Guess the number between 1 and 20.")
    print("Type 'x' to exit, 's' to show the secret number (cheat), 'd' to toggle debug mode, 'm' to toggle move mode (number shifts after each guess), or 'n' to start a new game with a new number")

    while True:
        if debug_mode:
            print(f"[DEBUG] Current secret number: {secret_number}")

        user_input = input("Enter your guess: ").strip().lower()

        if user_input == 'x':
            print("You exited the game.")
            break

        elif user_input == 's':
            print(f"The secret number is: {secret_number}")
            continue

        elif user_input == 'd':
            debug_mode = toggle_flag(debug_mode)
            print(f"Debug mode {'enabled' if debug_mode else 'disabled'}.")
            continue

        elif user_input == 'm':
            move_mode = toggle_flag(move_mode)
            print(f"Move mode {'enabled' if move_mode else 'disabled'}.")
            continue

        elif user_input == 'n':
            secret_number = generate_secret_number()
            print("A new number has been generated.")
            continue

        elif is_valid_number(user_input):
            guess = int(user_input)
            message, correct = process_guess(guess, secret_number)
            print(message)

            if correct:
                break

            if move_mode:
                secret_number, shift = shift_number(secret_number)
                if debug_mode:
                    print(f"[DEBUG] Secret number changed by {shift} (move mode).")

        else:
            print("Invalid input. Please enter a number between 1 and 20, or 'x', 's', 'd', 'm', or 'n'.")

if __name__ == "__main__":
    main()
