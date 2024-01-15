#!/usr/bin/python3
"""This module creates a Class 'User'"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing Users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
