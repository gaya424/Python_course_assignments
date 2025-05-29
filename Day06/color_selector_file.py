import sys

colors = ['blue', 'green', 'yellow', 'white']

def display_menu():
    print("Please select a color:")
    for i, color in enumerate(colors, start=1):
        print(f"{i}: {color}")

def select_color_from_input():
    while True:
        user_input = input("Enter the number of the color: ").strip()
        if not user_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        choice = int(user_input)
        if 1 <= choice <= len(colors):
            return colors[choice - 1]
        else:
            print(f"Number must be between 1 and {len(colors)}.")

def select_color_from_arg(arg):
    if arg.isdigit():
        idx = int(arg)
        if 1 <= idx <= len(colors):
            return colors[idx - 1]
        else:
            print(f"Error: Number out of range (1 to {len(colors)}).")
            sys.exit(1)
    else:
        normalized = arg.lower()
        if normalized in colors:
            return normalized
        else:
            print(f"Error: '{arg}' is not a valid color.")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        color = select_color_from_arg(sys.argv[1])
    else:
        display_menu()
        color = select_color_from_input()

    print(f"Selected color: {color}")
