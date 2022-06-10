from fastapi import APIRouter, Request as RequestFastApi

from src.validators.get_starships_in_page_validator import get_starships_validator


starships_routes: APIRouter = APIRouter()


@starships_routes.get("/api/starships/list")
async def get_starships_in_page(request: RequestFastApi):
    """
    List of starships
    :param request:
    :return:
    """
    get_starships_validator(request)

    return {"message": "Hello World"}
