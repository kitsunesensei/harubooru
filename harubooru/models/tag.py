from enum import Enum
from uuid import UUID
from typing import Union
from pydantic import BaseModel


class TagTypes(str, Enum):
    ARTIST = 'artist'
    CHARACTER = 'character'
    COPYRIGHT = 'copyright'
    GENERAL = 'general'
    GENRE = 'genre'
    META = 'meta'
    STUDIO = 'studio'


class Tag(BaseModel):
    id: Union[int, str, UUID]
    tag: str
    tag_type: TagTypes
