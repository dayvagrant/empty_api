"""
API Service application initialization.
See all endpoints in 'routes' folder.
"""
from fastapi import FastAPI
from app.api.routes import API_ROUTER
from app.core.settings import settings


def get_app() -> FastAPI:
    """
    FastAPI app initialization.
    """
    fast_app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.is_debug,
    )
    fast_app.include_router(API_ROUTER)
    return fast_app


APP = get_app()
