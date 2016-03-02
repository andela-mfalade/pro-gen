import logging
import random

import pandas as pd

from utils import log_helper
logger = log_helper.CustomLogger(__file__)


class Generator(object):
    def __init__(self):
        logger.info("Creating New Generator Instance.")
        self.profile = {}
        self.job_list = []
        self.fern_names = []
        self.local_names = []
        self.orchid_names = []
        self.extract_file_contents()

    def create_new_bio(self):
        return {
            'name': self.create_new_name(),
            'job_title': self.create_job_title(),
        }

    def create_new_name(self):
        num_names = random.choice([2, 2, 1])
        random_names = random.sample(self.local_names, num_names)
        mid_name = random.choice(
            random.choice([self.fern_names, self.orchid_names])
        )
        if num_names > 1:
            return (' ' + mid_name + ' ').join(random_names)
        return random_names[-1] + ' ' + mid_name

    def create_job_title(self):
        job_prefixes = ['', 'Junior', 'Senior', '']
        job_prefix = random.choice(job_prefixes)
        job_title = random.choice(self.job_list)
        if job_prefix:
            return job_prefix + ' ' + job_title
        return job_title

    def extract_file_contents(self):
        file_path = 'resources/African-Names.csv'
        source_file_df = pd.read_csv(file_path)
        all_jobs = source_file_df['Jobs']
        all_ferns_series = source_file_df['Ferns']
        all_orchids_series = source_file_df['Orchids']
        all_names_series = source_file_df['African-names']
        valid_jobs_series = all_jobs.dropna()
        valid_names_series = all_names_series.dropna()
        valid_ferns_series = all_ferns_series.dropna()
        valid_orchids_series = all_orchids_series.dropna()
        self.job_list = valid_jobs_series.tolist()
        self.fern_names = valid_ferns_series.tolist()
        self.local_names = valid_names_series.tolist()
        self.orchid_names = valid_orchids_series.tolist()


if __name__ == '__main__':
    main()
