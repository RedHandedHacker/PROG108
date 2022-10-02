#!/usr/bin/env python3

"""
Scott Davis
Chapter 11 Assignment
PROG108 Summer 2022
Bellevue College
"""

from datetime import datetime


def collect_dates():
    """ calls get_date for each datetime object,
    verifies sequencing of objects, returns date1 and date2"""
    while True:
        user_date1 = get_date(1)
        user_date2 = get_date(2)
        try:
            if user_date1 > user_date2:
                raise ValueError
            return user_date1, user_date2
        except ValueError:
            print(f"{user_date1} is not before {user_date2}\nPlease try again!\n")


def get_date(number):
    """collect and verify each date, returns date"""
    while True:
        try:
            date_str = input(f"Enter date and time #{number} (MM/DD/YYYY HH:MM): ")
            user_date = datetime.strptime(date_str, "%m/%d/%Y %H:%M")
            # print(user_date)
            return user_date
        except ValueError:
            print("Not a valid date/time. Please use the correct format")


def calculate_delta(first_date, second_date):
    """receives two datetime objects, calculates and returns difference"""
    time_span = second_date - first_date
    # print(days)
    return time_span


def print_result(first_date, second_date, delta_dates):
    """receives two datetime objects, and difference to display to user"""
    delta_seconds = delta_dates.seconds
    delta_hours = int(delta_seconds / 3600)
    delta_days = delta_dates.days
    print(f"\nThe first date/time you chose was {first_date}")
    print(f"\nThe second date/time you chose was {second_date}")
    print(f"\nThe delta of the date/times is: {delta_dates}")
    print(f"\nDifference in Days: {delta_days:,d}"
          f"\nDifference in Hours: {delta_hours}")


def main():
    """main function"""
    print("\nWelcome to my program to calculate the difference between two date/times.\n"
          "Let's begin!\n")
    again = 'y'
    while again.lower() == 'y':
        user_dates = collect_dates()
        time_between = calculate_delta(user_dates[0], user_dates[1])
        print_result(user_dates[0], user_dates[1], time_between)
        again = input("\nWould you like to calculate again(y/n)?")
    print("\n\nYou are so coola nd awesome, thanks for trying my program!")


if __name__ == '__main__':
    main()
