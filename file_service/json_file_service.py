import json
from typing import Any
from file_service.abstract_file_service import FileService


class JsonFileService(FileService):
    def get_data_from_file(self, filename: str) -> dict[str, Any]:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
