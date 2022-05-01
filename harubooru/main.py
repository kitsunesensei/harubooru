from fastapi import FastAPI
from harubooru.http.routers import file_router, tag_router

app = FastAPI()

app.include_router(file_router.router, prefix='/files')
app.include_router(tag_router.router, prefix='/tags')
