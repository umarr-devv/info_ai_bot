import logging

from src.config import Config

LOG_FORMAT = "%(name)s | %(asctime)s | %(funcName)s | %(filename)s | %(levelname)s | %(message)s"
LOG_FILE = '.log'


def set_logging(config: Config):
    logging.basicConfig(
        level=config.logging.level,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(filename=LOG_FILE, encoding='utf-8')
        ]
    )
