from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from harubooru.service_providers.database_provider import BaseModel


class TagMatchRule(BaseModel):  # pylint: disable=too-few-public-methods
    __tablename__ = 'tag_match_rules'
    search_string = Column(String, nullable=False, primary_key=True)
    use_tag = Column(String(length=36), ForeignKey('tags.id', onupdate='cascade', ondelete='cascade'), nullable=False)

    # Relationships
    tag = relationship("Tag", foreign_keys=[use_tag])
