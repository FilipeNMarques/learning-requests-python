from typing import Dict

from src.data.usecases.starships_list_colector import StarshipsListCollectorInterface
from src.presenters.interface.controllers import ControllersInterface


class StarShipListCollectorController(ControllersInterface):
    """
    Controller to list starships
    """

    def __init__(self, starship_list_collector: StarshipsListCollectorInterface):
        self.__use_case = starship_list_collector

    def handler(self, http_request: Dict) -> Dict:
        """
        Handler to list collector
        """
        page = http_request["query_params"]["page"]

        starships_list = self.__use_case.list(page)

        http_response = {"status_code": 200, "data": starships_list}

        return http_response
