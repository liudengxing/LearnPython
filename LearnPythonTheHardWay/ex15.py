from sys import argv
# Import argv

script, filename = argv
# Get filename, save as filename

txt = open(filename)
# Open file based on filename

print(f"Here's you file {filename} :")
print(txt.read())
# Print what have read

txt.close()

# Select file to read
print("Type the filename again:")
file_again = input("> ")


# Do what to do sa same sa just now
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
