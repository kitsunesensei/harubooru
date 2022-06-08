from typing import List
from fastapi import APIRouter, UploadFile, Body
from harubooru.http.validators.file_validator import FileMetaIn, FileOut
from harubooru.models.file import create_sha256_hash
from harubooru.models.file import File
from harubooru.models.media_types import get_media_type_by_mime, MediaType

router = APIRouter()


@router.get("/", response_model=List[FileOut])
async def query_files(query: str | None = None):
    return ""


@router.get("/{file_id}", response_model=FileOut)
async def get_file(file_id: str):
    return ""


@router.post("/", response_model=FileOut)
async def create_file(file: UploadFile):
    file_hash = await create_sha256_hash(file)

    #if existing_file := get_file_by_hash(file_hash):
    #    return existing_file

    media_type: MediaType = (get_media_type_by_mime(file.content_type))()

    media_dimensions = await media_type.get_dimensions(file)

    file_model = File(
        file_mime_type=media_type.get_mime_type(),
        file_hash=file_hash,
        media_width=media_dimensions.width,
        media_height=media_dimensions.height
    )

    return FileOut.from_orm(file_model)


@router.put("/{file_id}", response_model=FileOut)
async def create_file_meta(file_id: str, file: FileMetaIn = Body(...)):
    return file


@router.delete("/{file_id}", status_code=204)
async def delete_file(file_id: str):
    return ""
