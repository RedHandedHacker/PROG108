#!/usr/bin/env python3

"""
Scott Davis
Chapter 07 Assignment
PROG108 Summer 2022
Bellevue College2
"""

# import modules
import hw_07_module


# main function

def main():
    """ Main function calling functions from module
"""
    hw_07_module.show_food_menu()
    food_choice = hw_07_module.get_user_choice()
    hw_07_module.show_drink_menu()
    drink_choice = hw_07_module.get_user_choice()
    hw_07_module.show_dessert_menu()
    dessert_choice = hw_07_module.get_user_choice()
    total_price = hw_07_module.get_total_price(food_choice, drink_choice, dessert_choice)
    hw_07_module.print_total_price(total_price)
    hw_07_module.save_data(total_price)


main()
