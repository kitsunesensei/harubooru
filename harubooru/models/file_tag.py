from sqlalchemy import ForeignKey, Column, String, Integer, Enum as DbEnum
from sqlalchemy.orm import relationship
from harubooru.service_providers.database_provider import BaseModel
from harubooru.models.file import TriageStates


class FileTag(BaseModel):  # pylint: disable=too-few-public-methods
    __tablename__ = 'file_tags'
    file_id = Column(
        String(length=36),
        ForeignKey('files.id', onupdate='cascade', ondelete='cascade'),
        primary_key=True,
        nullable=False
    )
    tag_id = Column(
        String(length=36),
        ForeignKey('tags.id', onupdate='cascade', ondelete='cascade'),
        primary_key=True,
        nullable=False
    )
    triage_state = Column(DbEnum(TriageStates), nullable=False, default=TriageStates.PENDING)
    file_order_in_tag = Column(Integer, nullable=False, default=0)

    # Relationships
    file = relationship("File", back_populates="file_source", foreign_keys=[file_id])
    tag = relationship("Tag", back_populates="file_tag", foreign_keys=[tag_id])
