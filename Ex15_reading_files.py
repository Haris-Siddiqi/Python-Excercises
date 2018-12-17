# Ex 15
# Reading Files

# argv allows us to get user input from command line
from sys import argv
script, filename = argv
# Open the file and assign a variable to it
txt = open(filename)
# print(txt): TextIOWrapper name='feet.txt' mode='r'
print(f"Here's your file: {filename}\n")
# Reads file
print(txt.read())

# Part 2
print("Type the filename again:")
# File name
file_again = input("> ")
# Open and assign var to it
txt_again = open(file_again)
# Read file
x = txt_again.read()
print(x)
