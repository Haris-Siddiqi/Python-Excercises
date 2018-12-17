# Excercise 13
# The Argument Variable

# Import allows us to add modules to script from Python modules
# modules also callled libraries
# argv = argument variable, asks for input on the command line
from sys import argv
# Unpacks argv into script, ... , third
# argv must contain 3 arguments excluding script
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
