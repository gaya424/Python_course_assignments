import sys

def rot13(text):
    # Apply ROT13 transformation
    result = []
    for char in text:
        if 'a' <= char <= 'z':  # Lowercase letters
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  # Uppercase letters
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
    return ''.join(result)

def main():
    # Check if a string is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python rot13.py <string>")
        sys.exit(1)
    
    # Get the input string from the command-line arguments
    input_string = sys.argv[1]
    
    # Print the ROT13 version of the string
    print(rot13(input_string))

if __name__ == "__main__":
    main()