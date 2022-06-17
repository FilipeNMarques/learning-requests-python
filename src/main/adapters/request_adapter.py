from typing import Callable
from fastapi import Request as RequestFastApi


async def request_adapter(request: RequestFastApi, callback: Callable):
    """FastApi adapter
    :return: Testando a docstring
    """

    request_body = None

    try:
        request_body = await request.json()
    except:
        pass

    http_request = {"query_params": request.query_params, "body": request_body}

    http_response = callback(http_request)

    return http_response
