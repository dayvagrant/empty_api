from app.models.healthcheck import HealthcheckResult
from app.core.utils import return_current_time
from fastapi import APIRouter

ROUTER = APIRouter()


@ROUTER.get("/", )
def get_health_check() -> HealthcheckResult:
    """
    Healthcheck endpoint.
    """
    health_check = HealthcheckResult(is_alive=True)

    return {
        "health_check": health_check,
        "date": return_current_time()
        }
