"""Pydantic models for commmon Spotify objects"""

from enum import Enum

from pydantic import BaseModel


class ReleaseDatePrecision(str, Enum):
    """Precision of Release Date"""

    year = "year"  # pylint: disable=invalid-name
    month = "month"  # pylint: disable=invalid-name
    day = "day"  # pylint: disable=invalid-name


class RestrictionReason(str, Enum):
    """Reason for Restriction"""

    market = "market"  # pylint: disable=invalid-name
    product = "product"  # pylint: disable=invalid-name
    explicit = "explicit"  # pylint: disable=invalid-name


class Restrictions(BaseModel):
    """Restriction Spotify object"""

    reason: RestrictionReason


class ExternalUrls(BaseModel):
    """External Urls Spotify object"""

    spotify: str
