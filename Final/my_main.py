#!/usr/bin/env python3

"""
Scott Davis
Bellevue College
Summer 2022
PROG108 Final
"""

import my_module as m


def main():
    """Main Function"""
    user_string = m.get_string()
    str_len = m.get_length(user_string)
    m.display_values(str_len, user_string)


if __name__ == '__main__':
    main()
