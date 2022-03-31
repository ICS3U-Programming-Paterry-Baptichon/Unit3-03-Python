# Created by: Paterry Baptichon
# Created on : 2022-03-31
# This program is a guessing game where the user has to guess my age.


import constants


def main():
    # this function checks if there is over 30 students

    # input
    Lucky_number = int(input("How old do you think I am?: "))
    print("")

    # process & output
    if Lucky_number == constants.MY_LUCKY_NUMBER:
        print("correct")
    else:
      print("Not correct!")


if __name__ == "__main__":
    main()
  