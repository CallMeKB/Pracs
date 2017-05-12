"""
CP1404 Prac07 - Program to use guitar class in a meaningful way
"""

from prac07.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []
    valid = False
    while not valid:
        guitar_info = []
        name = input("Name: ")
        if name == "":
            valid = True
        else:
            guitar_info.append(name)
            guitar_info.append(int(input("Year: ")))
            guitar_info.append(float(input("Cost: ")))
            guitars.append(Guitar(guitar_info[0], guitar_info[1], guitar_info[2]))
    i = 0
    for guitar in guitars:
        i += 1
        print("Guitar {}: {} ({}), worth ${:10,.2f}".format(i, guitar.name, guitar.year, guitar.cost))

main()
