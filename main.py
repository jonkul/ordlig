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
            print("\nAdded grey letter:")
            print(str(a.g))
        elif inp == "y":
            a.yellow()
            print("\nAdded yellow letter:")
            print(str(a.y))
        elif inp == "gn":
            a.green()
            print("\nAdded green letter:")
            print(str(a.gn))
        elif inp == "c":
            a.g = []
            a.y = []
            a.gn = ["", "", "", "", ""]
            print("Filters cleared!")
        elif inp == "q":
            print("Bye, bye - and welcome back anytime!")
            return
        else:
            print("Please enter a valid choice!")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
