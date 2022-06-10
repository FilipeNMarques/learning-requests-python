from abc import ABC, abstractmethod
from typing import Tuple, Type, Dict
from requests import Request


class SwApiConsumerInterface(ABC):
    """API consumer interface"""

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        raise Exception("Must implement get_starships")
