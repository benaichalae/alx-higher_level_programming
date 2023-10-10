#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file"""
import sys
from os import path
import json
from typing import List


def save_to_json_file(my_obj, filename):
    """Saves a Python object as JSON to a file.

    Args:
        my_obj: The Python object to be serialized and saved as JSON.
        filename: The name of the file where
        the JSON representation of `my_obj` will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Loads a Python object from a JSON file.
    Reads the contents of a JSON file and converts it into a Python object.
    Args:
        filename: The name of the JSON file to be read
        and converted into a Python object.
    Returns:
        Any: The Python object obtained by deserializing
        the JSON content from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    args = sys.argv[1:]

    if path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    my_list.extend(args)

    save_to_json_file(my_list, "add_item.json")
