#!/usr/bin/env python3

"""
Scott Davis
Chapter 02 Assignment
PROG108 Summer 2022
Bellevue College
"""

def year_sequence():
    """
    Part 1
    """
    # Declare an variable and assign it the year your were born (or any number)
    # print the variable
    year = 2200
    print('  Original year:', year)

    # add 10 to the variable
    # print the variable
    year += 10
    print('         Add 10:', year)

    # subtract 100
    # print the variable
    year -= 100
    print('   Subtract 100:', year)

    # multiply it by 2
    # print the variable
    year *= 2
    print('  Mulitply by 2:', year)
    print()

def name_sequence():
    """
    Part 2
    """
    # Prompt the user for his/her name - use the input() function
    # assign the name to a variable
    # print the variable
    user_name = input("Please enter your name(s): ")
    print('\n   Unchanged: ', user_name)

    # split the variable to accomodate capitaizing multiple names
    # capitalize while iterating through the list
    print(' Capitalized: ', end=' ')
    split_user_name = user_name.split()
    for name in split_user_name:
        print(name.capitalize(), end=' ')
    print()

    # strip leading and trailing white space
    # print the variable
    user_name = user_name.strip()
    print('    Stripped: ', user_name)

    # all uppercase (wasn't sure if this is what was meant by capitalize so I included both)
    # print the variable
    user_name = user_name.upper()
    print('   Uppercase: ', user_name)

year_sequence()
name_sequence()
