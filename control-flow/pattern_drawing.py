# pattern_drawing.py

# Ask the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# While loop to iterate through each row
while row < size:
    # For loop to print asterisks for each column
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1
