from enum import Enum
from uuid import uuid4
from sqlalchemy import Column, String, DateTime, Enum as DbEnum
from sqlalchemy.orm import relationship
from harubooru.service_providers.database_provider import BaseModel


class SourceTypes(str, Enum):
    UPLOAD = 'upload'
    CLI = 'cli'
    INTERNET = 'internet'
    OTHER = 'other'


class Source(BaseModel):  # pylint: disable=too-few-public-methods
    __tablename__ = 'souces'
    id = Column(String(length=36), primary_key=True, nullable=False, default=uuid4)
    source_uri = Column(String, default=None)
    source_type = Column(DbEnum(SourceTypes), nullable=False, default=SourceTypes.OTHER)
    created_at = Column(DateTime(timezone=True), nullable=False, default='current_timestamp')

    # Relationships
    files = relationship("File", secondary="FileSource", back_populates="sources")
