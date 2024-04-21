from dataclasses import dataclass
from model.producer import Producer


@dataclass
class Producers:
    producers: list[Producer]

    def get_country_by_producer_id(self, producer_id: int) -> str:
        return next((producer.country for producer in self.producers if producer.id == producer_id), '')
