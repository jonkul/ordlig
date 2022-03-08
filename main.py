#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ordlig helper
"""

import menu as m
import analyzer as a

def main():
    """
    Runs the thing.
    """
    while True:
        m.menu()
        inp = input("\nChoice: ")

        if inp == "g":
            a.grey()
        elif inp == "y":
            a.yellow()
        elif inp == "gn":
            a.green()

        elif inp == "gr":
            a.greyrm()
        elif inp == "yr":
            a.yellowrm()
        elif inp == "gnr":
            a.greenrm()
        
        elif inp == "s":
            values = a.letter_frequency()
            print("The letters occur this many times in the dictionary:")
            for key, value in values.items():
                print(key + ":", value)

        elif inp == "c":
            a.clear()
            print("Filters cleared!")

        elif inp == "q":
            print("Bye, bye - and welcome back anytime!")
            return
        else:
            print("Please enter a valid choice!")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
