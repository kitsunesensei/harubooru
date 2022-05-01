from abc import ABCMeta
from typing import Tuple, NamedTuple, Type
from fastapi import UploadFile
import numpy as np
import cv2


class Dimensions(NamedTuple):
    width: int
    height: int


class MediaType(metaclass=ABCMeta):
    @staticmethod
    def get_mime_type() -> str:
        raise NotImplementedError('get_mime_type not implemented.')

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        raise NotImplementedError('get_file_extensions not implemented.')

    @staticmethod
    async def get_dimensions(file: UploadFile) -> Dimensions:
        raise NotImplementedError('get_dimensions not implemented.')

    @staticmethod
    def is_playable() -> bool:
        raise NotImplementedError('is_playable not implemented.')

    @classmethod
    def get_file_extension(cls) -> str:
        return cls.get_file_extensions()[0]

    @classmethod
    def mime_type_match(cls, mime_type_check: str) -> bool:
        return mime_type_check.lower() == cls.get_mime_type().lower()


class ImageType(MediaType, metaclass=ABCMeta):
    @staticmethod
    async def get_dimensions(file: UploadFile) -> Dimensions:
        await file.seek(0)
        nparr = np.asarray(bytearray(await file.read()), dtype="uint8")
        image = cv2.imdecode(buf=nparr, flags=cv2.IMREAD_UNCHANGED)
        height, width, _ = image.shape
        return Dimensions(width=width, height=height)

    @staticmethod
    def is_playable() -> bool:
        return False


class VideoType(MediaType, metaclass=ABCMeta):
    @staticmethod
    def is_playable() -> bool:
        return True


class Bmp(ImageType):
    @staticmethod
    def get_mime_type() -> str:
        return 'image/bmp'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('bmp',)


class Jpeg(ImageType):
    @staticmethod
    def get_mime_type() -> str:
        return 'image/jpeg'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('jpg', 'jpeg',)


class Png(ImageType):
    @staticmethod
    def get_mime_type() -> str:
        return 'image/png'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('png',)


class Svg(ImageType):
    @staticmethod
    def get_mime_type() -> str:
        return 'image/svg+xml'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('svg',)


class Webp(ImageType):
    @staticmethod
    def get_mime_type() -> str:
        return 'image/webp'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('webp',)


class Gif(ImageType):
    @staticmethod
    def get_mime_type() -> str:
        return 'image/gif'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('gif',)


class Mp4(VideoType):
    @staticmethod
    def get_mime_type() -> str:
        return 'video/mp4'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('mp4',)


class Mpeg(VideoType):
    @staticmethod
    def get_mime_type() -> str:
        return 'video/mpeg'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('mpeg',)


class Ogv(VideoType):
    @staticmethod
    def get_mime_type() -> str:
        return 'video/ogg'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('ogv',)


class Webm(VideoType):
    @staticmethod
    def get_mime_type() -> str:
        return 'video/webm'

    @staticmethod
    def get_file_extensions() -> Tuple[str, ...]:
        return ('webm',)


def get_media_type_by_mime(file_mime_type: str) -> Type[MediaType]:
    check_file_types: Tuple[Type[MediaType], ...] = (Bmp, Jpeg, Png, Svg, Webp, Gif, Mp4, Mpeg, Ogv, Webm,)

    for file_type in check_file_types:
        if file_type.mime_type_match(file_mime_type):
            return file_type

    raise ValueError('File Type not found.')
