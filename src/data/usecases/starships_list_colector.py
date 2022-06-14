from typing import Dict, List

from src.domain.usecases.starships_list_colector import StarshipsListCollectorInterface
from src.data.interfaces import SwApiConsumerInterface


class StarshipsListCollector(StarshipsListCollectorInterface):
    """Starships List Colector Usecase"""

    def __init__(self, api_consumer: SwApiConsumerInterface) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        """
        List come starships information
        :rtype: object
        :param page: int - number of the page
        :return: List with all starships information
        """

        api_response = self.__api_consumer.get_starships(page)
        starships_formatted_list = self.__format_api_response(
            api_response.response["results"]
        )

        return starships_formatted_list

    @classmethod
    def __format_api_response(cls, result: List[Dict]):
        """
        Format api response method
        :param result: List of starships information
        :return: A formatted list with data will be displayed to the user
        """

        starships_formatted_list = []

        for starship in result:
            starships_formatted_list.append(
                {
                    "id": starship["url"].split("/")[-2],
                    "name": starship["name"],
                    "model": starship["model"],
                    "max_atmosphering_speed": starship["max_atmosphering_speed"],
                    "hyperdrive_rating": starship["hyperdrive_rating"],
                    "MGLT": starship["MGLT"],
                }
            )

        return starships_formatted_list


1
