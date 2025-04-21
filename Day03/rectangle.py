import sys

# Check if both height and width are provided
if len(sys.argv) != 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)

# Get height and width from command-line arguments
try:
    height = float(sys.argv[1])
    width = float(sys.argv[2])
except ValueError:
    print("Please enter valid numbers for height and width.")
    sys.exit(1)

# Calculate the area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Print the results
print(f"The area of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")

