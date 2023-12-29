from sys import argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)

script, input_file = argv

currentFile = open(input_file)

print("First let's print the whole file:\n")
print_all(currentFile)

print("Now let's rewind, kind of like a tape.")
rewind(currentFile)

print("Now let's print three lines:")

for i in range(3):
    print(f"{i+1} ", currentFile.readline())