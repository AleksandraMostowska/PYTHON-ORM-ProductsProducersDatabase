from products_with_producers_service.products_with_producers import ProductsWithProducers
from file_service.json_file_service import JsonFileService
import logging
logging.basicConfig(level=logging.INFO)

def main() -> None:
    FILENAME = 'producers.json'
    data = ProductsWithProducers.get_products_with_producers(FILENAME, JsonFileService())

    logging.info(data)
    logging.info(data.get_country_with_most_expensive_products())

if __name__ == '__main__':
    main()