# Initialize a dictionary to count digits from 0 to 9
digit_counts = {str(d): 0 for d in range(10)}

input_str = input("Enter a list of numbers: ")

# Convert input into a list of integers
numbers = [int(num.strip()) for num in input_str.split(",")]

# Count digits
for number in numbers:
    for digit in str(number):
        if digit in digit_counts:
            digit_counts[digit] += 1

for digit in range(10):
    print(f"{digit}  {digit_counts[str(digit)]}")
