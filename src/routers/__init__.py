from fastapi import APIRouter

from .service import service_router

main_router = APIRouter()
main_router.include_router(service_router)
