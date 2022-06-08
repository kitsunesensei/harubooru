from pydantic import UUID4, root_validator
from harubooru.http.validators.base import BaseModel
from harubooru.models.tag import TagTypes


class TagIn(BaseModel):
    tag_en: str | None = None
    tag_jp: str | None = None
    tag_type: TagTypes
    auto_approve_files: bool = False
    auto_deny_files: bool = False

    @root_validator
    def tag_must_have_content(cls, values):  # pylint: disable=no-self-argument,no-self-use
        tag_en, tag_jp = values.get('tag_en'), values.get('tag_jp')
        if not (tag_en or tag_jp):
            raise ValueError('Tag must have content.')
        return values

    @root_validator
    def auto_values(cls, values):  # pylint: disable=no-self-argument,no-self-use
        auto_approve_files, auto_deny_files = values.get('auto_approve_files'), values.get('auto_deny_files')
        if auto_approve_files is True and auto_deny_files is True:
            raise ValueError('Auto approve and deny must not be activated together.')
        return values


class TagOut(TagIn):
    id: UUID4
