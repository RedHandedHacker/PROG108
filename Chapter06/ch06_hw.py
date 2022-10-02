#!/usr/bin/env python3

"""
Scott Davis
Chapter 06 Assignment
PROG108 Summer 2022
Bellevue College
"""

def get_total_numbers():
    """ Function returns total numbers to be averaged
    """
    print("How many total numbers?")
    return input()

def get_number_list(number_numbers):
    """ Function collects user numbers in a list
    """
    new_list = []
    for number in range(int(number_numbers)):
        print("\nEnter number", number + 1, ":")
        new_list.append(int(input()))
    return new_list

def get_average(user_list):
    """ Function averages list of numbers
    """
    return sum(user_list) / len(user_list)

def main():
    """ Main function to call other functions
    """
    again = "y"
    while again.lower() == "y":
        total_numbers = get_total_numbers()
        number_list = get_number_list(total_numbers)
        print("\nYour entered:", number_list)
        print("         Sum:", sum(number_list))
        print("     Average:",get_average(number_list))
        again = input("\nAgain (y/n)?\n")
    print("\nYou are so cool and awesome, thanks for coming!")

main()
