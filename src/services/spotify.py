"""Service to interact with the Spotify API"""

import base64
import os
from http import HTTPStatus
from typing import List, Optional

import requests

from src.exceptions.spotify import SpotifyApiException, SpotifyAuthTokenException
from src.models.spotify.response import (
    AccessTokenResponse,
    PaginatedSavedTracksResponse,
)
from src.models.spotify.track import SavedTrack
from src.models.spotify.user import User


class SpotifyClient:
    """Client to interact with Spotify Web API"""

    AUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
    USERS_TRACKS_URL = "https://api.spotify.com/v1/me/tracks?limit=50"
    CREATE_PLAYLIST_URL = "https://api.spotify.com/v1/users/{}/playlists"
    CURRENT_USER_PROFILE_URL = "https://api.spotify.com/v1/me"
    DEFAULT_TIMEOUT = 10

    def __init__(self, refresh_token: str) -> None:
        self.access_token = self._get_access_token(refresh_token)
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

    def _get_all_paginated_liked_songs(self, base_url: str) -> List[SavedTrack]:
        next_url: Optional[str] = base_url
        liked_songs: List[SavedTrack] = []
        while next_url:

            print(f"Getting liked songs at {next_url}")
            resp = requests.get(
                url=next_url,
                headers=self.headers,
                timeout=SpotifyClient.DEFAULT_TIMEOUT,
                params={"limit": "100"},
            )
            if resp.status_code != HTTPStatus.OK:
                raise SpotifyApiException(f"Error calling Spotify Api: {resp.json()}")

            resp = PaginatedSavedTracksResponse(**resp.json())
            liked_songs += resp.items

            next_url = resp.next

        return liked_songs

    def get_liked_songs(self) -> List[SavedTrack]:
        """Gets a users saved songs"""
        return self._get_all_paginated_liked_songs(
            SpotifyClient.USERS_TRACKS_URL
        )

    def create_playlist_and_add_songs(self, name: str, uris: List[str]) -> None:
        """Creates a spotify playlist with name :param: name
        Adds all :param: uris to playlist"""
        resp = requests.post(

        )

    def get_user_profile(self) -> User:
        resp = requests.get(
            url = SpotifyClient.CURRENT_USER_PROFILE_URL,
            headers=self.headers,
            timeout=SpotifyClient.DEFAULT_TIMEOUT
        )

        if resp.status_code != HTTPStatus.OK:
            raise SpotifyApiException(f"Error calling Spotify Api: {resp.json()}")
        
        return User(**resp.json())

    def _get_access_token(self, refresh_token: str) -> str:
        """Get Spotify access token"""
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        authorization = base64.b64encode(
            f"{os.environ['CLIENT_ID']}:{os.environ['CLIENT_SECRET']}".encode()
        ).decode()
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {authorization}",
        }

        resp = requests.post(
            url=SpotifyClient.AUTH_TOKEN_URL,
            headers=headers,
            data=payload,
            timeout=SpotifyClient.DEFAULT_TIMEOUT,
        )

        if resp.status_code != HTTPStatus.OK:
            raise SpotifyAuthTokenException(
                f"Error getting Spotify auth token: {resp.json()}"
            )

        resp = AccessTokenResponse(**resp.json())
        return resp.access_token
