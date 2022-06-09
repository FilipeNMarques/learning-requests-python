from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsListCollectorInterface(ABC):
    """Starship Collector Interface"""

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        raise Exception("Must implement list method")
