#!/usr/bin/python3
"""This module creates a Class 'Review'"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing Reviews"""

    place_id = ""
    user_id = ""
    text = ""
