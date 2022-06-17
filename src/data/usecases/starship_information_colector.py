from typing import Type, Dict
from src.domain.usecases.starship_information_colector import (
    StarshipInformationColectorInterface,
)
from src.data.interfaces.sw_api_consumer import SwApiConsumerInterface
from src.errors.http_unprecessable_entitity import HttpUnprecessableEntitity


class StarshipInformationColector(StarshipInformationColectorInterface):
    """_summary_

    _extended_summary_
    """

    def __init__(self, api_consumer: Type[SwApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_starship(self, starship_id: int, time: str) -> Dict:
        starship_infomation = self.__search_starship(starship_id)
        mglt = starship_infomation["MGLT"]

        distance_traveled = self.__claculate_distace_traveled(mglt, time)

        formatted_response = self.__format_response(
            starship_infomation, distance_traveled
        )

        return formatted_response

    def __search_starship(self, starship_id: int) -> Dict:
        api_response = self.__api_consumer.get_starship_information(starship_id)

        if api_response.response["MGLT"] == "unknown":
            raise HttpUnprecessableEntitity("Inexistent starship id, sorry.")

        return api_response.response

    @classmethod
    def __claculate_distace_traveled(cls, mgtl: str, time: str) -> int:
        distance_traveled = int(mgtl) * int(time)

        return distance_traveled

    @classmethod
    def __format_response(
        cls, starship_information: Dict, distance_travaled: int
    ) -> Dict:

        return {
            "starship": starship_information["name"],
            "model": starship_information["model"],
            "manufacturer": starship_information["manufacturer"],
            "max_atmosphering_speed": starship_information["max_atmosphering_speed"],
            "MGLT": starship_information["MGLT"],
            "distance_travaled": f"{str(distance_travaled)} ML",
        }
