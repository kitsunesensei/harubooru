from pydantic import BaseModel as Super


class BaseModel(Super):
    class Config:  # pylint: disable=too-few-public-methods
        orm_mode = True
