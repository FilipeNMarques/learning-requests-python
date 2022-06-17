from src.infra.sw_api_consumer import SwApiConsumer
from src.data.usecases import StarshipInformationColector
from src.presenters.controllers import StarshipInformationColectorController


def get_starship_information_composer():
    """get_starship_information_by_id _summary_

    _extended_summary_
    """

    infra = SwApiConsumer()
    usecase = StarshipInformationColector(infra)
    controller = StarshipInformationColectorController(usecase)

    return controller
