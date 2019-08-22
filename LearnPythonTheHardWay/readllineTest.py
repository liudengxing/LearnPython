file = open('test.txt', 'r')

text_line = file.readline()
print(text_line)
text_line = file.readline()
print(text_line)
text_line = file.readline()
print(text_line)

file.seek(0)

text_line = file.readline()
print(text_line)
