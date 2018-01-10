import logging.config
import yaml


def setup_logging():
    with open('logging.yaml', 'r') as f:
        c = yaml.load(f.read())
        logging.config.dictConfig(c)
