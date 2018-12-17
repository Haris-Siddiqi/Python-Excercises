# Ex 16
# Reading Files

# Get file from command line
from sys import argv
script, filename = argv

# Printing
print(f"We're going to erase {filename}.")
print("If you're down hit CTRL-C.")
print("If you're not then press ENTER.")
input("Type here: ")

# Opent the file in write mode
print("\nOpening the file...")
target = open(filename, 'w')

# Erase file contents
print("Truncating the file. Goodbye!")
target.truncate()

# Input for writing to file
print("\nNow I'm going to ask you for three lines.\n")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Write to file
print("I'm going to write theese to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close file
print("And finally, we close it.")
target.close()
