from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsListCollectorInterface(ABC):
    """Starship Collector Interface"""

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        """list _summary_

        _extended_summary_

        Parameters
        ----------
        page : int
            _description_

        Returns
        -------
        List[Dict]
            _description_

        Raises
        ------
        Exception
            _description_
        """

        raise Exception("Must implement list method")
