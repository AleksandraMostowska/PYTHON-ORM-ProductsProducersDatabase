from producer_service.producers import Producers, Producer
from file_service.abstract_file_service import FileService
from dataclasses import dataclass


@dataclass
class ProducersFileReader:
    file_srv: FileService

    def get_producers(self, filename: str) -> Producers:
        data = self.file_srv.get_data_from_file(filename)
        producers = [Producer.get_producer_from_dict(producer_data) for producer_data in data['producers']]
        return Producers(producers)
