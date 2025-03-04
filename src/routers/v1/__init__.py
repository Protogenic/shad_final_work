from fastapi import APIRouter

from .books import books_router
from .sellers import sellers_router

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(books_router)
v1_router.include_router(sellers_router)