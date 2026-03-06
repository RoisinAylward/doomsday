#core_logic.py
# This file contains the core logic for the project. It will be used to implement the main functionality of the project.

#imports WIP

#Week day variables:


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
