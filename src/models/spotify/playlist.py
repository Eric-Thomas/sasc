"""Pydantic model for Spotify playlist object"""

from typing import Optional, List
from src.models.spotify.base import Item
from src.models.spotify.common import ExternalUrls
from src.models.spotify.followers import Followers
from src.models.spotify.image import Image
from src.models.spotify.user import User
from src.models.spotify.track import Track

class Playlist(Item):
    """Playlist Spotify object"""

    collaborative: bool
    description: Optional[str] = None
    external_urls: ExternalUrls
    followers: Followers
    images: List[Image]
    name: str
    owner: User
    public: bool
    snapshot_id: str
    tracks: List[Track]
