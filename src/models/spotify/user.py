"""Pydantic model for Spotify user object"""

from src.models.spotify.base import Item
from src.models.spotify.common import ExternalUrls
from src.models.spotify.followers import Followers
from typing import Optional

class User(Item):
    """User Spotify object"""
    external_urls: ExternalUrls
    followers: Followers
    display_name: Optional[str] = None