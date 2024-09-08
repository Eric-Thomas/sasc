"""Pydantic model for Spotify followers object"""

from pydantic import BaseModel
from typing import Optional

class Followers(BaseModel):
    """Followers Spotify object"""
    href: Optional[str] = None
    total: int