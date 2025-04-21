import math
import sys

# Check if a radius was provided
if len(sys.argv) != 2:
    print("Usage: python script.py <radius>")
    sys.exit(1)

# Get the radius from command-line arguments
try:
    radius = float(sys.argv[1])
except ValueError:
    print("Please enter a valid number for the radius.")
    sys.exit(1)

# Calculate the area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")

