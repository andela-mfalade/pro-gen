import time

import markovify

from config import pathto
from scripts import bio_server
from utils import file_utils
from utils import log_utils

server = bio_server.BioServer()
logger = log_utils.CustomLogger(__file__)


def word_join(self, words):
    sentence = " ".join(word.split("::")[0] for word in words)
    return sentence


def create_paragraph(file_path):
    with open(file_path) as f:
        file_content = f.read()
    model = markovify.Text(file_content, state_size=3)
    return ' '.join([model.make_short_sentence(140) for i in range(5)])


def combine_files():
    file_1 = pathto['CITY_NEIGHBORHOOD_PROCESSED']
    file_2 = pathto['GROWING_CITY_PROCESSED']
    file_3 = pathto['GROWING_CITY_NEIGHBORHOOD']
    file_utils.shuffle(file_1, file_2, file_3)

    file_a = pathto['PLANET_FRONDS_PROCESSED']
    file_b = pathto['THE_PLANET_PROCESSED']
    file_c = pathto['THE_PLANET_FRONDS']
    file_utils.shuffle(file_a, file_b, file_c)

    logger.info("File Merge Complete.")


def replace_file_contents():
    planet_in = pathto['THE_PLANET']
    planet_out = pathto['THE_PLANET_PROCESSED']
    file_utils.insert_values(planet_in, planet_out, server)

    gcity_in = pathto['GROWING_CITY']
    gcity_out = pathto['GROWING_CITY_PROCESSED']
    file_utils.insert_values(gcity_in, gcity_out, server)

    planet_fronds_in = pathto['PLANET_FRONDS']
    planet_fronds_out = pathto['PLANET_FRONDS_PROCESSED']
    file_utils.insert_values(planet_fronds_in, planet_fronds_out, server)

    c_neighborhood_in = pathto['CITY_NEIGHBORHOOD']
    c_neighborhood_out = pathto['CITY_NEIGHBORHOOD_PROCESSED']
    file_utils.insert_values(c_neighborhood_in, c_neighborhood_out, server)

    logger.info("File Contents Replacement Complete.")


def fetch_profile(num_profiles=1):
    city_file = pathto['CITY_NEIGHBORHOOD_PROCESSED']
    def compile_profile(index):
        return {
            'id': index + 1,
            'name': server.fetch_new_name(),
            'occupation': server.fetch_job_title(),
            'neighborhood': server.fetch_new_district(),
            'city_desc': create_paragraph(city_file),
            'neighborhood_desc': create_paragraph(city_file),
        }
    return [compile_profile(i) for i in range(num_profiles)]
