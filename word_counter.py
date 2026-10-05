filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    words = content.split()
    count = len(words)

    print("Total number of words:", count)

except FileNotFoundError:
    print("File not found.")