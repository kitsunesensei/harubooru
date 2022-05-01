from sqlalchemy import ForeignKey, Column, String, DateTime
from sqlalchemy.orm import relationship
from harubooru.service_providers.database_provider import BaseModel


class FileSource(BaseModel):  # pylint: disable=too-few-public-methods
    __tablename__ = 'file_sources'
    file_id = Column(
        String(length=36),
        ForeignKey('files.id', onupdate='cascade', ondelete='cascade'),
        nullable=False,
        primary_key=True
    )
    source_id = Column(
        String(length=36),
        ForeignKey('sources.id', onupdate='cascade', ondelete='cascade'),
        nullable=False,
        primary_key=True
    )
    source_file_name = Column(String, default=None)
    source_file_created_at = Column(DateTime(timezone=True), default=None)
    created_at = Column(DateTime(timezone=True), nullable=False, default='current_timestamp')

    # Relationships
    file = relationship("File", back_populates="file_source", foreign_keys=[file_id])
    source = relationship("Source", back_populates="file_source", foreign_keys=[source_id])
