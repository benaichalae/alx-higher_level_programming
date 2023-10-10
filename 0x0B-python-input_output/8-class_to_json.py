#!/usr/bin/python3
"""Defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure"""
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
