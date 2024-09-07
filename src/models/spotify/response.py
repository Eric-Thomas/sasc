"""Pydantic models for Spotify API responses"""

from typing import List, Optional

from pydantic import BaseModel

from src.models.spotify.base import Item
from src.models.spotify.track import SavedTrack


class AccessTokenResponse(BaseModel):
    """Model for success response for Spotify access token endpoint"""

    access_token: str
    token_type: str
    scope: str
    expires_in: int


class PaginatedResponse(BaseModel):
    """Model for Spotify API paginated response"""

    href: str
    limit: int
    next: Optional[str] = None
    offset: int
    previous: Optional[str] = None
    total: int
    items: List[Item]


class PaginatedSavedTracksResponse(PaginatedResponse):
    """Model for Spotify API saved tracks paginated response"""

    items: List[SavedTrack]
