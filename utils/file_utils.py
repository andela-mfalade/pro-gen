"""Combine contents of two text files.

This module shuffles lines of text found within two text files
"""

from itertools import izip_longest


def shuffle(file1, file2, out_file):
    with open(out_file, 'w') as res, open(file1) as f1, open(file2) as f2:
        for line1, line2 in izip_longest(f1, f2, fillvalue=""):
            res.write("{} \n {}\n".format(line1.rstrip(), line2.rstrip()))


def insert_values(out_file, in_file):
    with open(out_file, 'w') as out_f, open(in_file) as in_f:
        for line in in_f.read():
            import ipdb; ipdb.set_trace()
