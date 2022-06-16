from abc import ABC, abstractmethod
from typing import Dict


class StarshipInformationColectorInterface(ABC):
    """StarshipInformationColectorInterface _summary_

    _extended_summary_

    Parameters
    ----------
    ABC : _type_
    _description_
    """

    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        """find_starship _summary_

        _extended_summary_

        Parameters
        ----------
        starship_id : int
            _description_

        Returns
        -------
        Dict
            _description_
        """

        raise Exception("Must implement find_starship method")
