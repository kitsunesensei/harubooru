from fastapi import Depends
from sqlalchemy.orm import Session
from harubooru.models.file import File


def get_file_by_hash(file_hash: str, db_connection: Session = Depends()) -> File | None:
    return db_connection.query(File).filter(File.file_hash == file_hash).scalar()
