#!/usr/bin/env python3

"""
Scott Davis
Chapter 09 and 10 Assignment
PROG108 Summer 2022
Bellevue College
"""

import csv
import time


def get_template(template_location):
    """function to load template - returns template as list"""
    email_list = []
    with open(template_location, encoding='utf8') as file:
        for line in file:
            line = line.replace("\n", "")
            email_list.append(line)
    return email_list


def access_csv(csv_file, template):
    """function to loop through csv file"""
    print("Creating your emails...please wait.\n\n")
    time.sleep(2)
    with open(csv_file, newline="", encoding='utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            first_name = row[0].capitalize()
            email_address = row[2]
            print_email(first_name, email_address, template)


def print_email(first_name, email_address, template):
    """function to insert data into template and print"""
    for line in template:
        line = line.replace("{email}", email_address)
        line = line.replace("{first_name}", first_name)
        print(line)
    time.sleep(1)
    print('\n')


def get_csv_location():
    """function to gather location of csv source file"""
    csv_file_location = str(input(
        "Please enter location of csv file (default = email.csv): ") or "emails.csv")
    print("\n", csv_file_location, "\n")
    time.sleep(1)
    return csv_file_location


def get_template_location():
    """function to gather location of email template file"""
    template_file_location = str(input(
        "Please enter location of email template (default = email_template.txt): ")
                                 or "email_template.txt")
    print("\n", template_file_location, "\n")
    time.sleep(1)
    return template_file_location


def main():
    """Main function"""
    run_again = "y"
    while run_again == "y":
        csv_file_name = get_csv_location()
        template_file_name = get_template_location()
        template_list = get_template(template_file_name)
        access_csv(csv_file_name, template_list)
        run_again = input("Run again (y/n)?")
        print("\n")
    print("You are so awesome and cool, thanks for using my program")


if __name__ == '__main__':
    main()
