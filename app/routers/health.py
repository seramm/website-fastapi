from typing import Literal
from typing_extensions import TypedDict
from fastapi import APIRouter, status

STATUS = Literal["success", "error", "partial", "unknown"]


class ReturnHealtcheckStruct(TypedDict):
    status: STATUS


router = APIRouter(
    prefix="/v1/health-check",
    tags=["Health Check"],
)


@router.get(
    "/liveness",
    summary="Perform a health check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=ReturnHealtcheckStruct,
)
async def liveness() -> ReturnHealtcheckStruct:
    return {"status": "success"}
