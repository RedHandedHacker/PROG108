#!/usr/bin/env python3

"""
Scott Davis
Chapter 03.1 Assignment
PROG108 Summer 2022
Bellevue College
"""

# Program to convert month number to name

# Main function
def main():
    """
    Main Function
    """
    try_again = "y"
    while try_again.lower() == "y":
        # Gather user input
        user_input = (input("Please enter a number representing a month (1-12): \n"))
        # Verify user input
        user_month = int(user_input)
        if user_month > 12 or user_month < 1:
            print("Error: Please try again with a number from 1 to 12\n")
        # Display Month
        for month_match in range(1, 13):
            if user_month == month_match:
                print("\n" + MONTH_LIST[month_match-1] + "\n")
        try_again = input("Run again (y/n)? ")
        print()
    print("You are so cool and awesome, thanks for using my program!")

# Create list of months and execute main()
MONTH_LIST = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "Novemeber", "December"]
main()
