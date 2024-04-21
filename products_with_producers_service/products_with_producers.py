from dataclasses import dataclass
from collections import defaultdict
from decimal import Decimal
from file_service.abstract_file_service import FileService

from file_service.producers_json_file_reader import ProducersFileReader
from model.product import Product
from producer_service.producers import Producers
from typing import Self

@dataclass
class ProductsWithProducers:
    products: list[Product]
    producers: Producers

    def get_country_with_most_expensive_products(self) -> list[str]:
        countries_with_prices = defaultdict(Decimal)
        for product in self.products:
            producers_id = product.producer_id
            producers_country = Producers.get_country_by_producer_id(self.producers, producers_id)
            countries_with_prices[producers_country] += product.price
        biggest_prices = max(countries_with_prices.values())
        return [c for c, p in countries_with_prices.items() if p == biggest_prices]


    @classmethod
    def get_products_with_producers(cls, filename: str, file_srv: FileService) -> Self:
        file_reader = ProducersFileReader(file_srv)
        return cls(products=Product.get_all(), producers=file_reader.get_producers(filename))

    def __str__(self) -> str:
        return f'PRODUCTS: {self.products}\nPRODUCERS: {self.producers}'