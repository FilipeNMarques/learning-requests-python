from typing import Type, Dict

from src.data.usecases.starships_list_colector import StarshipsListCollectorInterface


class StarShipListCollectorController:
    """
    Controller to list starships
    """

    def __int__(self, starship_list_collector: Type[StarshipsListCollectorInterface]):
        self.__use_case = starship_list_collector

    def handle(self, http_request: Dict) -> Dict:
        """
        Handler to list collector
        """
        page = http_request["query_params"]["page"]

        starships_list = self.__use_case.list(page)

        http_response = {"status_code": 200, "data": starships_list}

        return http_response
