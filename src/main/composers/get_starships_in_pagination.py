from src.infra.sw_api_consumer import SwApiConsumer
from src.data.usecases import StarshipsListCollector
from src.presenters.controllers import StarShipListCollectorController


def get_starships_in_paginagion():
    """get_starships_in_paginagion _summary_

    _extended_summary_

    Returns
    -------
    _type_
        _description_
    """

    infra = SwApiConsumer()
    usecase = StarshipsListCollector(infra)
    controller = StarShipListCollectorController(usecase)

    return controller
