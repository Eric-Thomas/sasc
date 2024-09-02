"""Pydantic models for Spotify Artist object"""
from pydantic import BaseModel

from src.models.spotify.common import ExternalUrls


class Artist(BaseModel):
    """Base class for Spotify Artist object"""

    external_urls: ExternalUrls
    name: str
