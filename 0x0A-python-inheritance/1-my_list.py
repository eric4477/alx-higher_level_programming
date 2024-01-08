#!/usr/bin/python3
"""
==========================
Module with class MyList
==========================

"""


class MyList(list):
    """
    class the inherits from List
    with print_sorted method

    """
    def print_sorted(self):
        """Methot that sorted a list"""
        print(sorted(list(self)))
