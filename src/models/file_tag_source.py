from pydantic import BaseModel
from file import File
from tag import Tag
from file_source import FileSource


class FileTagSource(BaseModel):
    file: File
    tag: Tag
    source: FileSource
