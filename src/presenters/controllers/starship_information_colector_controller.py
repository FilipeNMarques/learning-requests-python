from typing import Dict, Type

from src.presenters.interface import ControllersInterface
from src.domain.usecases import StarshipInformationColectorInterface


class StarshipInformationColectorController(ControllersInterface):
    """StarshipInformationColectorController _summary_

    _extended_summary_

    Parameters
    ----------
    ControllersInterface : _type_
        _description_
    """

    def __init__(
        self, starship_information_colector: Type[StarshipInformationColectorInterface]
    ) -> None:
        self.__use_case = starship_information_colector

    def handler(self, http_request: Dict):
        """handler _summary_

        _extended_summary_

        Parameters
        ----------
        http_request : Dict
            _description_
        """

        starship_id = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_information = self.__use_case.find_starship(starship_id, time)

        http_response = {"status_code": 200, "data": {"data": starship_information}}

        return http_response
