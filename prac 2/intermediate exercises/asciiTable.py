LOWER = 33
UPPER = 127

character = input("Enter a character: ")
print("The ASCII code for {} is: {}".format(character, ord(character)))

number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

while number <= LOWER or number >= UPPER:
    print("You must enter a number BETWEEN {} and {}".format(LOWER, UPPER))
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

print("The character for {} is: {}".format(number, chr(number)))

current_cell = LOWER
for i in range(95):
    print("{} {:>5}".format(current_cell, chr(current_cell)))
    current_cell += 1