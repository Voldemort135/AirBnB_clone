#!/usr/bin/python3
import cmd, uuid, datetime
from models import storage

class BaseModel:
    """The Class from which other Classes Inherit"""
    
    def __init__(self, *args, **kwargs):
        """Initializes the Instance Attributes"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the string representation of attributes"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the instance 'updated_at'"""

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary of all key/value pairs"""

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary

    
