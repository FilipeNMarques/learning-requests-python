from collections import namedtuple
from faker import Faker

fake = Faker(["pt_BR"])


def mock_starships():
    """
    Mock data for starships
    :return - dict of starship information with faker help
    """
    return {
        "name": fake.name(),
        "model": fake.name(),
        "manufacturer": fake.name(),
        "cost_in_credits": fake.random_int(),
        "length": fake.random_int(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
        "url": f"https://swapi.dev/api/starships/{fake.random_int()}/",
    }


class SwApiConsumerSpy:

    """
    Spy for sw apiconsumer
    :return - mock response with the same data structure
    """

    def __init__(self) -> None:
        self.get_starships_response = namedtuple(
            "GET_Starships", ["status_code", "request", "response"]
        )
        self.get_starships_attributes = {}

    def get_starships(self, page: int) -> any:
        self.get_starships_attributes["page"] = page

        return self.get_starships_response(
            status_code=200,
            request=None,
            response={
                "results": [
                    mock_starships(),
                    mock_starships(),
                    mock_starships(),
                    mock_starships(),
                    mock_starships(),
                ]
            },
        )
