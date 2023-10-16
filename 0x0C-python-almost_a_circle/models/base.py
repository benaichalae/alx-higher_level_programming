#!/usr/bin/python3
"""Base class module"""

import json
import os


class Base:
    """Base of all classes in this project"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Sets private attributes and id fields

        Args:
            _id (int): An integer
        """
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        if not all(isinstance(d, dict) for d in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        objects = [o.to_dictionary() for o in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(objects))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        ret = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
            for d in list_dicts:
                instance = cls(1, 1)
                instance.update(**d)
                ret.append(instance)
        return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to CSV a list of instances"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        attrs = ('id', 'size', 'width', 'height', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as f:
            for o in list_objs:
                d = o.to_dictionary()
                t = [str(d.get(attr, '')) for attr in attrs]
                f.write(",".join(t) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV"""
        filename = cls.__name__ + ".csv"

        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                instance = cls(1, 1)
                instance.update(*[int(x) for x in arguments])
                list_objs.append(instance)
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance
