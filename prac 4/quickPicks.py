import random


def main():
    number_of_quick_picks = int(input("How many quick picks?"))
    for i in range(number_of_quick_picks):
        picks = []
        for n in range(6):
            valid = False
            while not valid:
                pick = random.randint(1, 45)
                if pick in picks:
                    pass
                else:
                    picks.append(pick)
                    valid = True
        picks.sort()
        print("{:3}{:3}{:3}{:3}{:3}{:3}".format(picks[0], picks[1], picks[2], picks[3], picks[4], picks[5]))

main()
