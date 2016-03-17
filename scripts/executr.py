from threading import Thread
import Queue

from firebase import firebase

import markovify

from config import pathto
from config import valueof
from scripts import bio_server
from utils import file_utils
from utils import log_utils
from utils import thread_utils

server = bio_server.BioServer()
logger = log_utils.CustomLogger(__file__)
firebase = firebase.FirebaseApplication(valueof['DB_PATH'], None)
new_user = 'Ozgur Vatansever'


def bootstrap_files():
    replace_file_contents()
    combine_files()


def create_paragraph(file_path):
    with open(file_path) as f:
        file_content = f.read()
    model = markovify.Text(file_content, state_size=3)
    _x = valueof['NUM_SENTENCES']
    return ' '.join([model.make_short_sentence(140) for i in range(_x)])


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
    return fetch_profiles_in_chunks(num_profiles)


def get_profile_chunk(chunk_size, queue=None):
    city_file = pathto['GROWING_CITY_NEIGHBORHOOD']

    def compile_profile(index):
        return {
            'id': index + 1,
            'name': server.fetch_new_name(),
            'occupation': server.fetch_job_title(),
            'neighborhood': server.fetch_new_district(),
            'city_description': create_paragraph(city_file),
            'neighborhood_description': create_paragraph(city_file),
        }
    queue.put([compile_profile(i) for i in range(chunk_size)])


def fetch_profiles_in_chunks(num_profiles):
    queue = Queue.Queue()
    threads = []
    x = thread_utils.chunkate(num_profiles)
    for i in x:
        t = Thread(target=get_profile_chunk, args=(i, queue))
        threads.append(t)
        t.start()
        t.join()
    final_res = []
    for _ in range(queue.qsize()):
        final_res += queue.get()
    return final_res


def update_firebase(req_list):
    firebase.post(
        'requests',
        req_list,
    )
