"""Pydantic models for Spotify Album objects"""
from enum import Enum
from typing import List, Optional

from src.models.spotify.base import Item
from src.models.spotify.common import ExternalUrls, ReleaseDatePrecision, Restrictions
from src.models.spotify.image import Image


class AlbumType(str, Enum):
    """Type of album"""

    album = "album"  # pylint: disable=invalid-name
    single = "single"  # pylint: disable=invalid-name
    compilation = "compliation"  # pylint: disable=invalid-name


class Album(Item):
    """Base class for Spotify Album object"""

    album_type: AlbumType
    total_tracks: int
    available_markets: Optional[List[str]]
    external_urls: ExternalUrls
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: ReleaseDatePrecision
    restrictions: Restrictions
