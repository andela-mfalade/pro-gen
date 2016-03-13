"""Hold all constants and file paths.

This exists to make file paths easily configurable within the program.
"""
import os

if os.environ['PROCESS_ENV'] == 'development':
    ROOT_DIR = ''
elif os.environ['PROCESS_ENV'] == 'production':
    ROOT_DIR = '/home/progen/pro-gen/'


valueof = {
    'LUCKY_NUM': 10,
    'NUM_SENTENCES': 5,
    'A_SAMPLE': 'AAAA',
    'X_SAMPLE': 'XXXX',
    'MAX_NAME_COUNT': 4,
    'WORD_SEPARATOR': ' ',
    'SENTENCE_SEPARATOR': '.',
}


pathto = {
    'THE_PLANET': ROOT_DIR + 'resources/ThePlanet.txt',
    'AFRICAN_NAMES': ROOT_DIR + 'resources/African-Names.csv',
    'GROWING_CITY': ROOT_DIR + 'resources/GrowingCity.txt',
    'PLANET_FRONDS': ROOT_DIR + 'resources/PlanetFronds.txt',
    'CITY_NEIGHBORHOOD': ROOT_DIR + 'resources/TheCityNeighborhood.txt',


    'FRONDS_PLANET_FILE': ROOT_DIR + 'resources/FrondsPlusPlanet.txt',
    'GROWING_NEIGHBORHOOD_FILE': ROOT_DIR + 'resources/GrowingPlusNeighborhood.txt',


    'THE_PLANET_PROCESSED': ROOT_DIR + 'results/ThePlanetProcessed.txt',
    'GROWING_CITY_PROCESSED': ROOT_DIR + 'results/GrowingCityProcessed.txt',
    'PLANET_FRONDS_PROCESSED': ROOT_DIR + 'results/PlanetFrondsProcessed.txt',
    'CITY_NEIGHBORHOOD_PROCESSED': ROOT_DIR + 'results/TheCityNeighborhoodProcessed.txt',


    'GROWING_CITY_NEIGHBORHOOD': ROOT_DIR + 'results/GrowintCity-Plus-CityNeighborhood.txt',
    'THE_PLANET_FRONDS': ROOT_DIR + 'results/ThePlanet-Plus-PlanetFronds.txt',
}
