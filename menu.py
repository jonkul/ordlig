"""
Functions for the menu.
"""

import analyzer as a

def menu():
    """
    Prints the menu and returns user input.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("::Text Analyzer Program::")
    print(
        """
        q)                Quit

        g)                Grey letters
        y)                Yellow letters
        gn)               Green letters

        gr)               Remove last grey
        yr)               Remove last yellow
        gnr)              Remove last green

        c)                Clear filters
        """
        )
    print("::Active filters::")
    print("\n       Greyed out letters: " + str(a.g))
    print("       Yellow letters: " + str(a.y))
    print("       Green letters: " + str(a.gn))
    print(a.ten())
