from src.data.usecases.starship_information_colector import StarshipInformationColector
from src.errors.defaultError import DefaultError
from src.infra.test.sw_api_consumer import SwApiConsumerSpy


def test_find_starship():
    """test_find_starship _summary_

    _extended_summary_
    """

    api_consumer = SwApiConsumerSpy()
    starship_information_colector = StarshipInformationColector(api_consumer)

    starship_id = 12
    time = 4

    response = starship_information_colector.find_starship(starship_id, time)

    assert (
        api_consumer.get_starship_information_attributes["starship_id"] == starship_id
    )
    assert "MGLT" in response
    assert "distance_travaled" in response
    assert isinstance(response, dict)


def test_find_starship_error():
    """test_find_starship_error _summary_

    _extended_summary_
    """

    api_consumer = SwApiConsumerSpy()
    starship_information_colector = StarshipInformationColector(api_consumer)
    starship_id = 31
    time = 4

    try:
        starship_information_colector.find_starship(starship_id, time)
    except DefaultError as err:
        assert err.message is not None
        assert isinstance(err, DefaultError)
