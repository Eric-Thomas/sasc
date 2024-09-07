"""Service to interact with the Spotify API"""

import base64
import os
from http import HTTPStatus

import requests

from src.exceptions.spotify import SpotifyAuthTokenException


class SpotifyClient:
    """Client to interact with Spotify Web API"""

    SPOTIFY_AUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
    DEFAULT_TIMEOUT = 10

    def __init__(self, refresh_token: str) -> None:
        self.access_token = self._get_access_token(refresh_token)

    def get_liked_songs(self) -> None:
        """Gets a users saved songs"""
        raise NotImplementedError

    def create_playlist(self, name: str) -> None:
        """Creates a spotify playlist with name :param: name"""
        raise NotImplementedError

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
            url=SpotifyClient.SPOTIFY_AUTH_TOKEN_URL,
            headers=headers,
            data=payload,
            timeout=SpotifyClient.DEFAULT_TIMEOUT,
        )

        if resp.status_code != HTTPStatus.OK:
            raise SpotifyAuthTokenException(
                f"Error getting Spotify auth token: {resp.json()}"
            )

        return resp.json()["access_token"]
