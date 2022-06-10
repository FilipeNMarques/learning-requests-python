from .starships_list_colector import StarshipsListCollector
from src.infra import SwApiConsumer


def test_list():
    api_consumer = SwApiConsumer()
    startships_list_colector = StarshipsListCollector(api_consumer)

    page = 1
    startships_list_colector.list(page)
