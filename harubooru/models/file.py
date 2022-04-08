from uuid import UUID
from datetime import datetime
from typing import Union
from pydantic import BaseModel


class File(BaseModel):
    id: Union[int, str, UUID]
    storage: str
    storage_path: str
    file_extension: str
    file_mime_type: str
    file_hash: str
    file_hash_1x2: str
    media_width: int
    media_height: int
    created_at: datetime

    def is_new(self):
        return self.id == ''
