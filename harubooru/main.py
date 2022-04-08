from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from models.file import File

app = FastAPI()


@app.get("/files", response_model=File)
async def index(query: Optional[str] = None):
    return File(
        id='test id',
        storage='test storage',
        storage_path='test path',
        file_extension='test extension',
        file_mime_type='test mime type',
        file_hash='test hash',
        file_hash_1x2='test hash 2',
        media_width=100,
        media_height=200,
        created_at=datetime(year=1990, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    )


@app.get("/files/{file_id}")
async def get_file():
    return {"item_id": item_id, "q": q}


@app.post("/files", response_model=File)
async def create_file(file: File):
    return file


@app.patch("/files/{file_id}", response_model=File)
async def update_file(file: File):
    return file


@app.delete("/files/{file_id}", response_model=File)
async def delete_file():
    return file
