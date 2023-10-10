#!/usr/bin/python3
"""Defines a function read_file."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
