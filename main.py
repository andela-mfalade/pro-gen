"""Progen entry point.

Main script to initiate biogenesis.
"""
import time

import markovify

from config import pathto
from config import valueof
from scripts import bio_server
from utils import file_utils


server = bio_server.BioServer()



def fetch_names(num_names):
    for i in range(num_names):
        bio = server.fetch_new_bio()
        print bio
        time.sleep(0.1)

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


def create_sentences_from_text_file(file_path):
    with open(file_path) as f:
        file_content = f.read()
    model = markovify.Text(file_content, state_size=3)

    for i in range(5):
        print ' '.join([model.make_short_sentence(140) for i in range(5)])
        print '\n'


def comine_files():
    file1 = pathto['THE_PLANET']
    file2 = pathto['PLANET_FRONDS']
    file3 = pathto['FRONDS_PLANET']
    file_utils.shuffle(file1, file2, file3)


def replace_contents():
    file1 = pathto['THE_PLANET']
    file2 = pathto['THE_PLANET_FILE_PROCESSED']
    file_utils.insert_values(file1, file2)


def main():
    fetch_names(valueof['LUCKY_NUM'])
    # create_sentences_from_text_file(pathto['THE_PLANET_FILE'])
    # comine_files()

if __name__ == '__main__':
    main()
