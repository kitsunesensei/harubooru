from pydantic import BaseModel
from file import File
from tag import Tag


class FileTag(BaseModel):
    file: File
    tag: Tag
    file_order_in_tag: int = 0
