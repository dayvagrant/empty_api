"""
Main router with all routers included.
"""
from app.api import healthcheck
from app.api import test_request
from fastapi import APIRouter

API_ROUTER = APIRouter()

API_ROUTER.include_router(healthcheck.ROUTER, tags=["healthcheck"], prefix="/healthcheck")
API_ROUTER.include_router(test_request.ROUTER, tags=["test_request"], prefix="/test_request")
