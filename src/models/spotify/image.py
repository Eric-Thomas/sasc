"""Pydantic model for Spotify Image object"""
from pydantic import BaseModel


class Image(BaseModel):
    """Image Spotify Object"""

    url: str
    height: int
    width: int
