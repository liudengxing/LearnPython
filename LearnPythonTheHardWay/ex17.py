from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()

print("Ready, hit RETURN to continue, CTRL-L to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all donw.")

out_file.close()
in_file.close()
