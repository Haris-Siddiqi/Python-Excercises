# Ex 20
# Functions and Files

# Get file from command line
from sys import argv
script, input_file = argv

# Print entire file
def print_all(f):
    print(f.read())

# Go to beginning of file
def rewind(f):
    f.seek(0)

# Prints a specific line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open file and print it
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
# Go to first line
print("Now let's rewind, kind of like a tape")
rewind(current_file)
# Print 1st line
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
# Print 2nd line
current_line = current_line + 1
print_a_line(current_line, current_file)
# Print 3rd line
current_line = current_line + 1
print_a_line(current_line, current_file)
