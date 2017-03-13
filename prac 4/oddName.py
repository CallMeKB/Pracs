
''' Keegan '''

name = input("Enter your name:")
while name == "":
    print("You must enter your name.")
    name = input("Enter your name:")
letter_count = 1
try:
    for i in range(len(name)):
        print(name[letter_count])
        letter_count += 2
except IndexError:
    print("End of name (:")
