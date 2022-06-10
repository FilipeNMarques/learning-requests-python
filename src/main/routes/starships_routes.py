from fastapi import APIRouter, Request as RequestFastApi


starships_routes: APIRouter = APIRouter()


@starships_routes.get("/api/starships/list")
async def get_starships_in_page(request: RequestFastApi):
    """
    List of starships
    :param request:
    :return:
    """
    print(request.query_params)

    return {"message": "Hello World"}
