#!/usr/bin/env python3

"""
Scott Davis
Chapter 12 Assignment
PROG108 Summer 2022
Bellevue College
"""


def read_file():
    """reads file and returns dictionary"""
    new_list = []
    with open("monthly_sales.txt", encoding='utf8') as file:
        for line in file:
            string = line.strip()
            string = string.split("\t")
            string[1] = int(string[1])
            new_list.append(string)
        new_dictionary = dict(new_list)
    return new_dictionary


def display_menu():
    """displays menu"""
    print("\nPress 1 for the Total Annual Sales")
    print("Press 2 for the Average Annual Sales")
    print("Press 3 for the Highest Monthly Sales\n")


def process_choice(user_choice, passed_dictionary):
    """prompts for choice and calls appropriate function"""

    if int(user_choice) == 1:
        total_annual_sales(passed_dictionary)
    elif int(user_choice) == 2:
        average_annual_sales(passed_dictionary)
    elif int(user_choice) == 3:
        highest_month_sales(passed_dictionary)


def validate_choice():
    """collects and validates user choice"""
    while True:
        try:
            choice = int(input("Choice: "))
            if choice in range(1, 4):
                return choice
        except ValueError:
            print(end="")
        print("That is not a valid choice, please try again!\n")


def total_annual_sales(processed_dictionary):
    """displays total annual sales"""
    total_sales = sum(processed_dictionary.values())
    print(f'Total Annual Sales: ${total_sales:,.2f}')

def average_annual_sales(processed_dictionary):
    """displays average annual sales"""
    average_sales = sum(processed_dictionary.values()) / len(processed_dictionary)
    print(f'Average Annual Sales: ${average_sales:,.2f}')


def highest_month_sales(processed_dictionary):
    """displays month with the highest sales"""
    highest_month = ""
    highest_sales = max(processed_dictionary.values())
    print(f'The Highest Monthly Sales: ${highest_sales:,.2f}')
    for month, value in processed_dictionary.items():
        if highest_sales == value:
            highest_month = month
    print("That month was: ", highest_month)


def main():
    """main function"""
    run_again = 'y'
    while run_again.lower() == 'y':
        source_dictionary = read_file()
        display_menu()
        valid_choice = validate_choice()
        process_choice(valid_choice, source_dictionary)
        run_again = input("\nWould you like to try again (y/n)? ")
    print("\nYou are so cool and awesome, thanks for using my program!")

if __name__ == '__main__':
    main()
