from fastapi import FastAPI

from entrypoints.routes.fazer_macarrao import macarrao_router

app = FastAPI()

app.include_router(macarrao_router)
