import copy
import logging
import random

import pandas as pd

from utils import log_helper
logger = log_helper.CustomLogger(__file__)


class BioServer(object):
    def __init__(self):
        logger.info("Creating New Generator Instance.")
        self.profile = {}
        self.jobs = []
        self.ferns = []
        self.names = []
        self.orchids = []
        self.extract_file_contents()

    def fetch_new_bio(self):
        return {
            'name': self.create_new_name(),
            'job_title': self.create_job_title(),
        }

    def create_new_name(self):
        ferns = copy.copy(self.ferns)
        orchids = copy.copy(self.orchids)
        num_names = random.choice([2, 2, 1])
        random_names = random.sample(self.names, num_names)
        mid_name = random.choice(random.choice([ferns, orchids]))
        new_names = ([mid_name], random_names)
        return self.format_names(new_names)

    def format_names(self, new_names):
        mid_name, others = new_names
        _mid_name = " ".join([self.remove_trailing_spaces(x) for x in mid_name])
        _other_names = [self.remove_trailing_spaces(x) for x in others]
        if len(_other_names) > 1:
            return (' ' + _mid_name + ' ').join(_other_names)
        return _other_names[-1] + ' ' + _mid_name

    def remove_trailing_spaces(self, string):
        empty_space = " "
        if string.startswith(empty_space):
            return string[1:]
        elif string.endswith(empty_space):
            return string[:-1]
        return string

    def create_job_title(self):
        job_prefixes = ['', 'Junior', 'Senior', '']
        job_prefix = random.choice(job_prefixes)
        job_title = random.choice(self.jobs)
        if job_prefix:
            return job_prefix + ' ' + job_title
        return job_title

    def extract_list(self, series_list):
        return (series.dropna().tolist() for series in series_list)

    def extract_file_contents(self):
        file_path = 'resources/African-Names.csv'
        source_file_df = pd.read_csv(file_path)
        jobs = source_file_df['Jobs']
        ferns = source_file_df['Ferns']
        orchids = source_file_df['Orchids']
        names = source_file_df['African-names']
        fields = [jobs, names, ferns, orchids]
        self.jobs, self.names, self.ferns, self.orchids = self.extract_list(fields)


if __name__ == '__main__':
    main()
