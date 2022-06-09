from typing import Type
import requests
from requests import Request
from collections import namedtuple


class SwApiConsumer:

    def __int__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')

    def get_starships(self, page: int) -> any:
        req = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships',
            params={"page": page}
        )
        req_prepared = req.prepare()
        response = self.__send_http_request(req_prepared)
        status_code = response.status_code


        return {
            'request': req,
            'status_code': status_code,
            'response': response.json()
        }

        # return self.get_starships_response(status_code=response.status_code, request=req, response=response.json())

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        http_session = requests.Session()
        response = http_session.send(req_prepared)

        return response
