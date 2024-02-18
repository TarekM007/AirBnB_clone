#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_objs = FileStorage.__objects

        new_dict = {}

        for obj in all_objs.keys():
            new_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    new_dict = json.load(file)

                    for key, value in new_dict.items():
                        class_name, obj_id = key.split('.')

                        _class = eval(class_name)

                        instance = _class(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
