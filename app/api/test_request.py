from app.models.model_test_request import TestRequest
from app.core.utils import return_current_time
from fastapi import APIRouter
import os

ROUTER = APIRouter()


@ROUTER.get("/")
def test_func_request(request_item):
    """
     endpoint.
    """
    folder, file = os.path.split(request_item)
    return {
        "request_item": request_item,
        "folder": folder,
        "file": file,
        "date": return_current_time()
        }
