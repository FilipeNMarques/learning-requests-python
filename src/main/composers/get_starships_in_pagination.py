from src.infra.sw_api_consumer import SwApiConsumer
from src.data.usecases.starships_list_colector import StarshipsListCollector
from src.presenters.controllers.starship_list_collector_controller import (
    StarShipListCollectorController,
)


def get_starships_in_paginagion():
    """Get starships composer"""

    infra = SwApiConsumer()
    usecase = StarshipsListCollector(infra)
    controller = StarShipListCollectorController(usecase)

    return controller
