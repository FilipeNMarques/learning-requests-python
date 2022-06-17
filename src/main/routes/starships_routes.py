from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.main.adapters import request_adapter

from src.validators import get_starships_validator
from src.validators import get_starship_information_validator

from src.main.composers import get_starship_information_composer
from src.main.composers import get_starships_in_paginagion

from src.presenters.errors import handle_error

starships_routes: APIRouter = APIRouter()


@starships_routes.get("/api/starships/list")
async def get_starships_in_page(request: RequestFastApi):
    """
    List of starships
    :param request:
    :return:
    """

    response = None
    controller = get_starships_in_paginagion()

    try:
        await get_starships_validator(request)
        response = await request_adapter(request, controller.handler)
    except Exception as error:
        response = handle_error(error)

    return JSONResponse(status_code=response["status_code"], content=response["data"])


@starships_routes.post("/api/starship/information")
async def get_starship_information(request: RequestFastApi):
    """get_starship_information _summary_

    _extended_summary_

    Parameters
    ----------
    request : RequestFastApi
        _description_

    Returns
    -------
    _type_
        _description_
    """

    response = None
    controller = get_starship_information_composer()

    try:
        await get_starship_information_validator(request)
        response = await request_adapter(request, controller.handler)
    except Exception as error:
        response = handle_error(error)

    return JSONResponse(status_code=response["status_code"], content=response["data"])
