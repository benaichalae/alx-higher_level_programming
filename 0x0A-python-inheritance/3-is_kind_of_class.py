#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.
    Args:
    obj: The object to check.
    a_class: The class to match the type of obj to.
    Returns:
    If obj is an instance or inherited of a_class - True.
    Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
