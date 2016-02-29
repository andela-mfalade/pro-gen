import logging
import random


logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.DEBUG)


def generate_random_name():
    logger.debug("Attempting to generate random name..")


def main():
    random_name = generate_random_name()


if __name__ == '__main__':
    main()
