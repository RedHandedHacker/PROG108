#!/usr/bin/env python3

"""
Scott Davis
Chapter 03.2 Assignment
PROG108 Summer 2022
Bellevue College
"""

def print_numbers():
    """
    Print even numbers from 0 to 100
    """
    for digit in range(0, 101, 2):
        print(digit, end=" ")

print_numbers()
