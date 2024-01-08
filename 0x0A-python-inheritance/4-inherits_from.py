#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a subclass of a_class;
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
