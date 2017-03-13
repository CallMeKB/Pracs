LOWER = 10
UPPER = 50

def main():
    character = input("Enter a character: ")
    print("The ASCII code for {} is: {}".format(character, ord(character)))
    number = get_number(LOWER,UPPER)
    print("The character for {} is: {}".format(number, chr(number)))

def get_number(lower, upper):
    while True:
        try:
            number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
            while number <= LOWER or number >= UPPER:
                print("You must enter a number BETWEEN {} and {}".format(LOWER, UPPER))
                number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
            break
        except ValueError:
            print("Please enter a valid number!")
    return number

main()
