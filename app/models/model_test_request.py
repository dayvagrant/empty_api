"""
Model for endpoint.
"""
from pydantic import BaseModel


class TestRequest(BaseModel):
    text: str
    is_alive: bool
