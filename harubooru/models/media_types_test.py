from pytest import raises
from harubooru.models.media_types import *


def test_media_type():
    with raises(NotImplementedError):
        MediaType.get_mime_type()
        MediaType.get_file_extensions()
        MediaType.get_dimensions()
        MediaType.is_playable()
        MediaType.get_file_extension()
        MediaType.mime_type_match('image/jpeg')


def test_image_type():
    assert ImageType.is_playable() is False


def test_video_type():
    assert VideoType.is_playable() is True


def test_get_media_type_by_mime():
    assert get_media_type_by_mime('image/jpeg') == Jpeg
    assert get_media_type_by_mime('image/JpEg') == Jpeg
    assert get_media_type_by_mime('image/jpeg'.upper()) == Jpeg

    with raises(ValueError):
        get_media_type_by_mime('crap')
        get_media_type_by_mime('image/jpeg ')
        get_media_type_by_mime(' image/jpeg')
