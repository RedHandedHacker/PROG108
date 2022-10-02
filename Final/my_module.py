#!/usr/bin/env python3

"""
Scott Davis
Bellevue College
Summer 2022
PROG108 Final
"""


def get_length(user_string):
    """Get length of string"""
    return len(user_string)


def get_string():
    """Get user input string"""
    return input("Please enter a string: ")


def display_values(user_number, user_string):
    """Display values"""
    print(f"Length of string: {user_number}")
    print(f"String: {user_string}")
