from dataclasses import asdict

from fastapi import APIRouter

from domain.groups.fazer_macarrao import fazer_macarrao_group

macarrao_router = APIRouter()


@macarrao_router.get("/fazer-macarrao/{quantidade}")
def fazer_macarrao_route(quantidade: int):
    macarrao = fazer_macarrao_group(quantidade)
    return asdict(macarrao)
