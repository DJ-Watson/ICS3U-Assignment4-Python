#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: October 2019
# program calculates the average between the numbers


def main():
    # input
    inp1 = input("enter the first number (0-100): ")
    inp2 = input("enter the second number (0-100): ")
    inp3 = input("enter the third number (0-100): ")

    # process and output
    try:
        num1 = int(inp1)
        num2 = int(inp2)
        num3 = int(inp3)
        if ((num1 < 0) | (num1 > 100) | (num2 < 0) | (num2 > 100) |
           (num3 < 0) | (num3 > 100)):
            print("")
            print("invalid input (integer is too big or too small)")
        else:
            answer = (num1 + num2 + num3)/3
            print("")
            print("average = {}".format(answer))
    except ValueError:
        print("")
        print("invalid input (input is not an integer)")


if __name__ == "__main__":
    main()
