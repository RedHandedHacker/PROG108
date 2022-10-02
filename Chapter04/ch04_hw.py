#!/usr/bin/env python3

"""
Scott Davis
Chapter 03.1 Assignment
PROG108 Summer 2022
Bellevue College
"""

#  Program ro calculate price of an order containing apples and bananas

# Define Functions

def get_number_fruit(type_fruit):
    '''
    Returns user input for number of fruit
    '''
    print("\nEnter the number of ", type_fruit, " in your bag: ")
    return input()

def calculate_price_apples(apples):
    '''
    Returns total cost of apples
    '''
    apples = int(apples) * 3
    return apples

def calculate_price_bananas(bananas):
    '''
    Returns total cost of bananas
    '''
    bananas = int(bananas) * 2
    return bananas

def display_prices(apples, bananas):
    '''
    Displays costs, total and goodbye message
    '''
    print("\n Your apples cost: $", apples)
    print("Your bananas cost: $", bananas)
    print("  Your total cost: $", apples + bananas)
    print("\nYou are so cool and amazing, thanks for shopping with us!")

def main():
    '''
    Gathers user input, calculates prices and displays prices, total, and goodby message
    '''
    run_again = "y"
    while run_again.lower() == "y":
        print()
        num_apples = get_number_fruit("apples")
        num_bananas = get_number_fruit("bananas")
        price_apples = calculate_price_apples(num_apples)
        price_bananas = calculate_price_bananas(num_bananas)
        display_prices(price_apples, price_bananas)
        run_again = input("Would you like to shop again? (y/n)")
    print("\nYou are so awesome, please come again!")

if __name__ == "__main__":
    main()
