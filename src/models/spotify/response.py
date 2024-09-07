"""Pydantic models for Spotify API responses"""

from pydantic import BaseModel


class AccessToken(BaseModel):
    """Model for success response for Spotify access token endpoint"""

    access_token: str
    token_type: str
    scope: str
    expires_in: int
