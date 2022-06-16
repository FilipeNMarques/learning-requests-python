from abc import ABC, abstractmethod
from typing import Tuple, Type, Dict
from requests import Request


class SwApiConsumerInterface(ABC):
    """API consumer interface"""

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """get_starships _summary_

        _extended_summary_

        Parameters
        ----------
        page : int
            _description_

        Returns
        -------
        Tuple[int, Type[Request], Dict]
            _description_

        Raises
        ------
        Exception
            _description_
        """

        raise Exception("Must implement get_starships")

    @abstractmethod
    def get_starship_information(
        self, starship_id: int
    ) -> Tuple[int, Type[Request], Dict]:
        """get_starship_information _summary_

        _extended_summary_

        Parameters
        ----------
        starship_id : int
            _description_

        Returns
        -------
        Tuple[int, Type[Request], Dict]
            _description_
        """

        raise Exception("Must implement get_startship_information")
