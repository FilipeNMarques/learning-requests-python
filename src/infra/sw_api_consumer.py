from typing import Dict, Tuple, Type
from collections import namedtuple
import requests
from requests import Request

from src.errors import HttpRequestError
from src.data.interfaces import SwApiConsumerInterface


class SwApiConsumer(SwApiConsumerInterface):
    """
    Class to consume star wars api with http requests
    """

    def __init__(self) -> None:
        self.get_starships_response = namedtuple(
            "GET_starships",
            ["status_code", "request", "response"],
        )
        self.get_starship_information_response = namedtuple(
            "GET_starship_info", ["status_code", "request", "response"]
        )

    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """
        Request starships with pagination
        :param page: int
        :return: request, status code and response attributes
        """

        req = requests.Request(
            method="GET", url="https://swapi.dev/api/starships", params={"page": page}
        )
        req_prepared = req.prepare()
        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >= 200) and (status_code <= 299):
            return self.get_starships_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()["detail"], status_code=status_code
            )

    def get_starship_information(
        self, starship_id: int
    ) -> Tuple[int, Type[Request], Dict]:
        """get_starship_information _summary_

        _extended_summary_

        Parameters
        ----------
        starship_id : int
            _description_

        Returns
        -------
        Tuple[int, Type[Request], Dict]
            _description_
        """

        req = requests.Request(
            method="GET",
            url=f"https://swapi.dev/api/starships/{starship_id}",
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if (status_code >= 200) and (status_code <= 299):
            return self.get_starship_information_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()["detail"], status_code=status_code
            )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        """
        Prepare a session and send http request
        :param req_prepared: Request Object with all params
        :return: Http response raw
        """

        http_session = requests.Session()
        response = http_session.send(req_prepared)

        return response
