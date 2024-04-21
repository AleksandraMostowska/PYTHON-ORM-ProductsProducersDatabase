from dataclasses import dataclass
from typing import Any, Self

@dataclass
class Producer:
    id: int
    name: str
    country: str

    @classmethod
    def get_producer_from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(id=data['id'], name=data['name'], country=data['country'])