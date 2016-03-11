"""Progen entry point.

Main script to initiate biogenesis.
"""

from scripts import executr
from config import pathto
from config import valueof




def main():
    executr.fetch_names(valueof['LUCKY_NUM'])
    # executr.create_sentences_from_text_file(pathto['THE_PLANET_PROCESSED'])
    # executr.replace_file_contents()
    # executr.combine_files()

if __name__ == '__main__':
    main()
