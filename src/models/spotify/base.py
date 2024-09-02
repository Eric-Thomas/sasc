"""Pydantic Base Model class for Spotify objects"""
from pydantic import BaseModel


class Identifiable(BaseModel):
    """Model for object identifiable with a Spotify ID"""

    id: str


class Item(Identifiable):
    """Base class for a Spotify Item"""

    href: str
    type: str
    uri: str
