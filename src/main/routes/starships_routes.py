from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.validators.get_starships_in_page_validator import get_starships_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers import get_starships_in_paginagion

starships_routes: APIRouter = APIRouter()


@starships_routes.get("/api/starships/list")
async def get_starships_in_page(request: RequestFastApi):
    """
    List of starships
    :param request:
    :return:
    """
    get_starships_validator(request)

    controller = get_starships_in_paginagion()

    response = await request_adapter(request, controller.handler)

    return JSONResponse(
        status_code=response["status_code"], content={"data": response["data"]}
    )
