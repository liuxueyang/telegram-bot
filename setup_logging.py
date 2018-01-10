import logging.config
import yaml
import os


def setup_logging():
    if not os.path.exists('log'):
        os.mkdir('log')

    with open('logging.yaml', 'r') as f:
        c = yaml.load(f.read())
        logging.config.dictConfig(c)
