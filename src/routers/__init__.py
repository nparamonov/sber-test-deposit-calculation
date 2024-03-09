from fastapi import APIRouter

from .deposit import deposit_router
from .service import service_router

main_router = APIRouter()
main_router.include_router(service_router)
main_router.include_router(deposit_router)
