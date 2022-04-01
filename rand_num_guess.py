#!/usr/bin/env python3

# Created by Paterry Bpatichon Junior
# Created 2022-03-31
# This program prompts a user to guess a number
# and tells them if they are correct or not (random number).

import random


def main():
    # this function gets a guess then checks if it is right

    # input
    guessed_number = int(input("Enter a number between 0 and 10: "))

    # process & output
    random_number = random.randint(0, 10)  # a number between 0 and 9
    if guessed_number == random_number:
        print("Correct!")
    else:
        print(
            "Not correct, the answer is {}.".format(random_number)
        )


if __name__ == "__main__":
    main()