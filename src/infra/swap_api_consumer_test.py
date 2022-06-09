from src.infra.swap_api_consumer import SwApiConsumer


def test_get_starships():
    swapi_consumer = SwApiConsumer()
    page = 1
    get_starship_response = swapi_consumer.get_starships(page=1)

    assert get_starship_response['request'].method == 'GET'
    assert get_starship_response['request'].url == 'https://swapi.dev/api/starships'
    assert get_starship_response['request'].params == {'page': page}
    assert get_starship_response['status_code'] == 200
    assert isinstance(get_starship_response['response']['results'], list)
