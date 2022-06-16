from src.errors.httprequesterror import HttpRequestError
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


def test_get_starship_information(requests_mock):
    """
    test_get_starship_information _summary_

    _extended_summary_
    """

    starship_id = 12
    sw_api_consumer = SwApiConsumer()

    requests_mock.get(
        f"https://swapi.dev/api/starships/{starship_id}",
        status_code=200,
        json={
            "model": "T-65 X-wing",
            "manufacturer": "Incom Corporation",
            "max_atmosphering_speed": "1050",
            "hyperdrive_rating": "1.0",
            "MGLT": "100",
        },
    )

    starship_information = sw_api_consumer.get_starship_information(starship_id)

    assert starship_information.request.method == "GET"
    assert (
        starship_information.request.url
        == f"https://swapi.dev/api/starships/{starship_id}"
    )
    assert starship_information.status_code == 200

    assert "MGLT" in starship_information.response
