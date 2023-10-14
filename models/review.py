#!/usr/bin/python3
"""
module review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representation

    args:
        place_id: (str) will be Place.id
        user_id: (str) will be User.id
        text: (str)
    """
    place_id = ""
    user_id = ""
    text = ""
