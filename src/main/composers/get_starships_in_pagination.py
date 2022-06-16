from src.infra.sw_api_consumer import SwApiConsumer
from src.data.usecases.starships_list_colector import StarshipsListCollector
from src.presenters.controllers.starship_list_collector_controller import (
    StarShipListCollectorController,
)


def get_starships_in_paginagion():
    """get_starships_in_paginagion _summary_

    _extended_summary_

    Parameters
    ----------
    v1 : int
        _description_
    v1 : str
        _description_

    Returns
    -------
    _type_
        _description_
    """

    infra = SwApiConsumer()
    usecase = StarshipsListCollector(infra)
    controller = StarShipListCollectorController(usecase)

    return controller
