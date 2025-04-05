import math

# Ask the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))
    
# Calculate the area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
    
# Print the results
print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")
