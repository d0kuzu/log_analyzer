from abc import ABC, abstractmethod
from typing import Dict

class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: Dict[str, Dict[str, int]]) -> None:
        pass
