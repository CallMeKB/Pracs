import random


def main():
    number_of_quick_picks = int(input("How many quick picks?"))
    for i in range(number_of_quick_picks):
        picks = [(str(random.randint(1, 99)))for n in range(6)]
        print(' '.join(picks))

main()