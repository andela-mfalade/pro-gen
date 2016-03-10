"""Combine contents of two text files.

This module shuffles lines of text found within two text files
"""

from itertools import izip_longest
import re

from config import valueof


def shuffle(file1, file2, out_file):
    with open(out_file, 'w') as res, open(file1) as f1, open(file2) as f2:
        for line1, line2 in izip_longest(f1, f2, fillvalue=""):
            res.write("{} \n {}\n".format(line1.rstrip(), line2.rstrip()))


def insert_values(in_file, out_file, server):

    def transform(word):
        if valueof['A_SAMPLE'] in word:
            new_district = server.fetch_new_district()
            return re.sub(r"AAA+", new_district, word)
        if valueof['X_SAMPLE'] in word:
            new_name = server.fetch_new_name()
            return re.sub(r"XXX+", new_name, word)
        return word

    with open(in_file) as in_f, open(out_file, 'w') as out_f:
        for line in in_f:
            tokens = line.split(valueof['WORD_SEPARATOR'])
            new_word = ' '.join([transform(x) for x in tokens])
            out_f.write(new_word)
