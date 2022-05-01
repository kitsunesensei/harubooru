from sqlalchemy.orm import Session
from harubooru.models.file import File


def get_file_by_hash(db: Session, file_hash: str) -> File | None:
    return db.query(File).filter(File.file_hash == file_hash).scalar()
