"""Progen entry point.

Main script to initiate biogenesis.
"""
import argparse
import codecs
import sqlite3
import time

from markov.db import Db
from markov.gen import Generator
from markov.parse import Parser
from markov.rnd import Rnd
from markov.sql import Sql
from scripts import bio_server


server = bio_server.BioServer()

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '


def fetch_names(num_names):
    for i in range(num_names):
        bio = server.fetch_new_bio()
        print bio
        time.sleep(0.3)

def fetch_random_paragraphs(db_name, num_paragraphs):
    for i in range(num_paragraphs):
        db = Db(sqlite3.connect(db_name + '.db'), Sql())
        generator = Generator(db_name, db, Rnd())
        p_l = [generator.generate(WORD_SEPARATOR) for i in range(num_paragraphs)]
        print '\n'.join(p_l)
        time.sleep(0.3)
        print '\n'

def create_chain(db_name, file_path, num_rows):
    db = Db(sqlite3.connect(db_name + '.db'), Sql())
    db.setup(lucky_num)

    txt = codecs.open(file_path, 'r', 'utf-8').read()
    Parser(db_name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(txt)


def main():
    parser = argparse.ArgumentParser()
    usage = 'usage >> python %s <mode>\nMode can be either "parse" or "gen"'
    parser.add_argument('--mode', help=usage)
    args = parser.parse_args()
    mode = args.mode

    db_name = 'markov_test'
    lucky_num = 5
    file_path = 'resources/GrowingCity.txt'

    # fetch_names(lucky_num)

    if mode == 'parse':
        create_chain(db_name, file_path, lucky_num)
    elif mode == 'gen':
        paragraphs = fetch_random_paragraphs(db_name, lucky_num)
    else:
        raise ValueError(usage)


if __name__ == '__main__':
    main()
