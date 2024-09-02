"""Pydantic models for Spotify Track object"""
from datetime import datetime
from typing import List, Optional

from src.models.spotify.album import Album
from src.models.spotify.artist import Artist
from src.models.spotify.base import Item
from src.models.spotify.common import ExternalIds, ExternalUrls, Restrictions


class TrackLink(Item):
    """Relinked track Spotify object"""

    external_urls: dict


class Track(Item):
    """Base class for Spotify Track object"""

    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    linked_from: Optional[TrackLink]
    restrictions: Restrictions
    name: str
    popularity: str
    preview_url: Optional[str]
    track_number: int
    is_local: bool


class SavedTrack(Track):
    """Saved Track Spotify object"""

    added_at: datetime
