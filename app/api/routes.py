"""
Main router with all routers included.
"""
from app.api import healthcheck
from fastapi import APIRouter

API_ROUTER = APIRouter()

API_ROUTER.include_router(healthcheck.ROUTER, tags=["healthcheck"], prefix="/healthcheck")
