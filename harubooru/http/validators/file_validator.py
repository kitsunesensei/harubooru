from typing import List
from datetime import datetime
from pydantic import UUID4, HttpUrl
from harubooru.http.validators.base import BaseModel
from harubooru.http.validators.tag_validator import TagIn, TagOut
from harubooru.models.file import File, TriageStates
from harubooru.models.source import SourceTypes
from harubooru.lib.media_types import get_media_type_by_mime, MediaType


class FileSourceIn(BaseModel):
    source_uri: str
    source_type: SourceTypes
    source_file_name: str | None = None
    created_at: datetime


class FileMetaIn(BaseModel):
    tags: List[UUID4] | None = None
    create_tags: List[TagIn] | None = None
    source: FileSourceIn | None = None


class FileSourceOut(FileSourceIn):
    id: UUID4


class FileOut(BaseModel):
    id: UUID4
    media_url: HttpUrl
    media_width: int
    media_height: int
    file_extension: str
    file_mime_type: str
    file_hash: str
    file_hash_1x2: str
    triage_state: TriageStates
    created_at: datetime
    is_playable: bool
    tags: List[TagOut]
    sources: List[FileSourceOut]
