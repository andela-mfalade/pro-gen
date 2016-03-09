"""Progen entry point.

Main script to initiate biogenesis.
"""
import codecs
import time

from markov.parse import Parser
from scripts import bio_server


server = bio_server.BioServer()

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '


def main():
    for i in range(5):
        bio = server.fetch_new_bio()
        print "Profile %d >> " % i, bio
        time.sleep(0.3)
    file_path = 'resources/GrowingCity.txt'
    txt = codecs.open(file_path, 'r', 'utf-8').read()
    name = 'growing_city'
    Parser(name, depth=8, ssc=SENTENCE_SEPARATOR, wsc=WORD_SEPARATOR).parse(txt)


if __name__ == '__main__':
    main()
