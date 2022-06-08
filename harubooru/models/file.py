from enum import Enum
from hashlib import sha256
from uuid import uuid4
from fastapi import UploadFile
from sqlalchemy import Column, CheckConstraint, String, Integer, DateTime, Enum as DbEnum
from sqlalchemy.orm import relationship
from harubooru.service_providers.database_provider import BaseModel


class TriageStates(str, Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    DENIED = 'denied'


class File(BaseModel):  # pylint: disable=too-few-public-methods
    __tablename__ = 'files'
    id = Column(String(length=36), primary_key=True, nullable=False, default=uuid4)
    storage = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    file_mime_type = Column(String, nullable=False)
    file_hash = Column(String, nullable=False)
    file_hash_1x2 = Column(String, default=None)
    media_width = Column(Integer, nullable=False)
    media_height = Column(Integer, nullable=False)
    triage_state = Column(DbEnum(TriageStates), nullable=False, default=TriageStates.PENDING)
    created_at = Column(DateTime(timezone=True), nullable=False, default='current_timestamp')

    # Relationships
    tags = relationship("Tag", secondary="FileTag", back_populates="files")
    sources = relationship("Source", secondary="FileSource", back_populates="files")

    CheckConstraint('media_width > 0')
    CheckConstraint('media_height > 0')


async def create_sha256_hash(file: UploadFile) -> str:
    buff_size = 65536  # lets read stuff in 64kb chunks!
    file_hash = sha256()

    while chunk := await file.read(buff_size):
        file_hash.update(chunk)

    return f'(sha256){file_hash.hexdigest()}'
