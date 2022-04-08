from uuid import UUID
from datetime import datetime
from typing import Union
from pydantic import BaseModel
from file import File


class FileSource(BaseModel):
    id: Union[int, str, UUID]
    file: File
    source_url: str
    source_file_name: str
    source_created_at: datetime
    created_at: datetime
