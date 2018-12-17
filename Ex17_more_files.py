# Ex 17
# Copying Files

# Import argv to get files from command line
# Import exists to check if output file exists
from sys import argv
from os.path import exists
script, from_file, to_file = argv

# Open from_file and read data into indata
print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()

# Each character in indata is one byte
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
input("Ready, hit ENTER to contine, CTRL-C to abort." )

# Write indata to to_file
out_file = open(to_file, 'w')
out_file.write(indata)

# CLose files
print("Alright, all done.")
out_file.close()
in_file.close()
