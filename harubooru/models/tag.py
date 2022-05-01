from uuid import uuid4
from enum import Enum
from sqlalchemy import Column, CheckConstraint, String, Boolean, Enum as DbEnum
from sqlalchemy.orm import relationship
from harubooru.service_providers.database_provider import BaseModel


class TagTypes(str, Enum):
    ARTIST = 'artist'
    CHARACTER = 'character'
    COPYRIGHT = 'copyright'
    GENERAL = 'general'
    GENRE = 'genre'
    META = 'meta'
    STUDIO = 'studio'


class Tag(BaseModel):  # pylint: disable=too-few-public-methods
    __tablename__ = 'tags'
    id = Column(String(length=36), primary_key=True, nullable=False, default=uuid4)
    tag_en = Column(String, nullable=True)
    tag_jp = Column(String, nullable=True)
    tag_type = Column(DbEnum(TagTypes), nullable=False, default=TagTypes.GENERAL)
    auto_approve_files = Column(Boolean, nullable=False, default=False)
    auto_deny_files = Column(Boolean, nullable=False, default=False)

    # Relationships
    files = relationship("File", secondary="FileTag", back_populates="tags")

    CheckConstraint('auto_approve_files != True AND auto_approve_files != auto_deny_files')
