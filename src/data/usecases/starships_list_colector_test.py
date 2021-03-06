from src.infra.test.sw_api_consumer import SwApiConsumerSpy
from .starships_list_colector import StarshipsListCollector


def test_list() -> None:
    """
    test_list _summary_

    _extended_summary_
    """
    api_consumer = SwApiConsumerSpy()
    startships_list_colector = StarshipsListCollector(api_consumer)

    page = 1
    response = startships_list_colector.list(page)

    assert api_consumer.get_starships_attributes == {"page": page}
    assert isinstance(response, list)
    assert "id" in response[0]
    assert "MGLT" in response[-1]
