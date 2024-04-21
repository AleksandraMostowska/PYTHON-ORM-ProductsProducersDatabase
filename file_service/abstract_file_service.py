from abc import ABC, abstractmethod
from typing import Any


class FileService(ABC):
    @abstractmethod
    def get_data_from_file(self, filename: str) -> dict[str, Any]:
        pass
