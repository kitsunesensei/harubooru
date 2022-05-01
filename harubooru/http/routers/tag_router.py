from uuid import uuid4
from typing import List
from fastapi import APIRouter
from harubooru.http.validators.tag_validator import TagIn, TagOut

router = APIRouter()


@router.get("/", response_model=List[TagOut])
async def search(search_term: str | None = None):
    return ""


@router.get("/{tag_id}", response_model=TagOut)
async def get_tag(tag_id: str):
    return ""


@router.post("/", response_model=TagOut)
async def create_tag(tag: TagIn):
    return TagOut(id=uuid4(), tag=tag.tag, tag_type=tag.tag_type, auto_approve_files=tag.auto_approve_files, auto_deny_files=tag.auto_deny_files)


@router.delete("/{tag_id}", status_code=204)
async def delete_tag(tag_id: str):
    return ""
