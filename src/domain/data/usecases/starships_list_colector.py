from typing import Dict, List

from src.domain.usecases.starships_list_colector import StarshipsListCollectorInterface
from src.infra import SwApiConsumer


class StarshipsListCollector(StarshipsListCollectorInterface):
    """Starships List Colector Usecase"""

    def __init__(self, api_consumer: SwApiConsumer) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        print(response)
