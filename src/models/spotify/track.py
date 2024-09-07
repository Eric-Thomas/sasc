"""Pydantic models for Spotify Track object"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from src.models.spotify.album import Album
from src.models.spotify.artist import Artist
from src.models.spotify.base import Item
from src.models.spotify.common import ExternalUrls, Restrictions


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
    external_ids: dict
    external_urls: ExternalUrls
    linked_from: Optional[TrackLink] = None
    restrictions: Optional[Restrictions] = None
    name: str
    popularity: int
    preview_url: Optional[str] = None
    track_number: int
    is_local: bool


class SavedTrack(BaseModel):
    """Saved Track Spotify object"""

    added_at: datetime
    track: Track
