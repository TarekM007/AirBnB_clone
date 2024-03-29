#!/usr/bin/python3

"""
BaseModel class that defines all common attributes/methods
for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance."""
        dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, dtime_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that contains all
        keys/values of the instance"""
        updated_dict = self.__dict__.copy()
        updated_dict["__class__"] = self.__class__.__name__
        updated_dict["created_at"] = self.created_at.isoformat()
        updated_dict["updated_at"] = self.updated_at.isoformat()

        return updated_dict

    def __str__(self):
        """Returns a readable string representation
        of BaseModel instances"""
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
