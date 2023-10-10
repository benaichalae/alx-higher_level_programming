#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                If None, all attributes are retrieved.

        Returns:
            dict: A dictionary containing requested attribute of the student.
        """
        if attrs is None:
            result_dict = self.__dict__
        else:
            result_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result_dict[attr] = getattr(self, attr)
        return result_dict
