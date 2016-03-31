"""Hold all constants and file paths.

This exists to make file paths easily configurable within the program.
"""
import os

if os.environ['PROCESS_ENV'] == 'development':
    ROOT_DIR = ''
elif os.environ['PROCESS_ENV'] == 'production':
    ROOT_DIR = '/home/senongo/progen/'


valueof = {
    'NUM_SENTENCES': 5,
    'A_SAMPLE': 'AAAA',
    'X_SAMPLE': 'XXXX',
    'MAX_NAME_COUNT': 4,
    'WORD_SEPARATOR': ' ',
    'SENTENCE_SEPARATOR': '.',
    'DB_PATH': 'https://progen.firebaseio.com/'
}


pathto = {
    'THE_PLANET': ROOT_DIR + 'resources/ThePlanet_v02.txt',
    'AFRICAN_NAMES': ROOT_DIR + 'resources/African-Names.csv',
    'GROWING_CITY': ROOT_DIR + 'resources/GrowingCity_v02.txt',
    'PLANET_FRONDS': ROOT_DIR + 'resources/PlanetFronds_v02.txt',
    'CITY_NEIGHBORHOOD': ROOT_DIR + 'resources/TheCityNeighborhood_v02.txt',


    'THE_PLANET_PROCESSED': ROOT_DIR + 'results/ThePlanetProcessed_v02.txt',
    'GROWING_CITY_PROCESSED': ROOT_DIR + 'results/GrowingCityProcessed_v02.txt',
    'PLANET_FRONDS_PROCESSED': ROOT_DIR + 'results/PlanetFrondsProcessed_v02.txt',
    'CITY_NEIGHBORHOOD_PROCESSED': ROOT_DIR + 'results/TheCityNeighborhoodProcessed_v02.txt',


    'THE_PLANET_FRONDS': ROOT_DIR + 'results/ThePlanet-Plus-PlanetFronds_v02.txt',
    'GROWING_CITY_NEIGHBORHOOD': ROOT_DIR + 'results/GrowintCity-Plus-CityNeighborhood_v02.txt',
}
