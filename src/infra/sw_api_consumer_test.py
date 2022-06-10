from src.errors import HttpRequestError
from src.infra.sw_api_consumer import SwApiConsumer


def test_get_starships(requests_mock):
    """Testing get_starships method with success"""

    requests_mock.get(
        "https://swapi.dev/api/starships",
        status_code=200,
        json={"some": "test", "results": [{}]},
    )

    swapi_consumer = SwApiConsumer()
    page = 1
    get_starship_response = swapi_consumer.get_starships(page)

    assert get_starship_response.request.method == "GET"
    assert get_starship_response.request.url == "https://swapi.dev/api/starships"
    assert get_starship_response.request.params == {"page": page}
    assert get_starship_response.status_code == 200
    assert isinstance(get_starship_response.response["results"], list)


def test_get_starships_error(requests_mock):
    """Testing get_starships method with error"""

    requests_mock.get(
        "https://swapi.dev/api/starships",
        status_code=404,
        json={"detail": "Not found", "results": [{}]},
    )

    swapi_consumer = SwApiConsumer()
    page = 1343

    try:
        swapi_consumer.get_starships(page)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
        print(error)
