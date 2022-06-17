from abc import ABC, abstractmethod
from typing import Dict


class ControllersInterface(ABC):
    """ControllersInterface _summary_

    _extended_summary_

    Parameters
    ----------
    ABC : _type_
        _description_

    Raises
    ------
    Exception
        _description_
    """

    @abstractmethod
    def handler(self, http_request: Dict):
        """handler _summary_

        _extended_summary_

        Parameters
        ----------
        http_response : _type_
            _description_
        Dict : _type_
            _description_

        Raises
        ------
        Exception
            _description_
        """

        raise Exception("Should implemente handler method")
