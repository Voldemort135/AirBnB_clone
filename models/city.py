#!/usr/bin/python3
"""This module creates a Class 'City'"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing Cities"""

    state_id = ""
    name = ""
