# Ex 23
# File Analysis

# define variables with argv
import sys
script, encoding, error = sys.argv

# Calls print_line function on each line in file
# which encodes text to bytes and vive versa
def main(language_file, encoding, errors):
    # reads one line from file
    line = language_file.readline()
    # call print_line function as long as line is not empty
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# Prints the text encoded to bytes and vice versa
def print_line(line, encoding, errors):
    # removes \n from line string
    next_lang = line.strip()
    # Encode language into raw bytes
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # Decode bytes to language
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    # Print the conversion
    print(raw_bytes, "<===>", cooked_string)

# Open file and call main function
languages = open("languages.txt", encoding = "utf- 8")
main(languages, encoding, error)
