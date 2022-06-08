from fastapi import FastAPI
from harubooru.service_providers.database_provider import get_session as db_session
from harubooru.http.routers import file_router, tag_router

app = FastAPI(
    dependencies=[db_session]
)

app.include_router(file_router.router, prefix='/files')
app.include_router(tag_router.router, prefix='/tags')
