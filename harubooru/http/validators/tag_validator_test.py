from pytest import raises
from harubooru.http.validators.tag_validator import TagIn, TagTypes


def test_tag_must_not_be_empty_validator():
    TagIn(tag_en='Test', tag_type=TagTypes.GENERAL)
    TagIn(tag_jp='Test', tag_type=TagTypes.GENERAL)

    with raises(ValueError):
        TagIn(tag_en=None, tag_type=TagTypes.GENERAL)
        TagIn(tag_en='   ', tag_type=TagTypes.GENERAL)
        TagIn(tag_jp=None, tag_type=TagTypes.GENERAL)
        TagIn(tag_jp=' ', tag_type=TagTypes.GENERAL)


def test_auto_values_must_not_be_truthy_together_validator():
    TagIn(tag_en='Not the Problem', tag_type=TagTypes.GENERAL, auto_approve_files=True, auto_deny_files=False)
    TagIn(tag_en='Not the Problem', tag_type=TagTypes.GENERAL, auto_approve_files=False, auto_deny_files=True)

    with raises(ValueError):
        TagIn(tag_en='Not the Problem', tag_type=TagTypes.GENERAL, auto_approve_files=True, auto_deny_files=True)
