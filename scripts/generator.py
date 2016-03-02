import logging
import random

import pandas as pd

from utils import log_helper
logger = log_helper.CustomLogger(__file__)


class Generator(object):
    def __init__(self):
        logger.info("Creating New Generator Instance.")
        self.profile = {}
        self.local_names = []
        self.mid_names = []
        self.state = 'idle'
        self.extract_names_from_file()

    def create_new_bio(self):
        return {
            'name': self.create_new_name(),
            'job_title': self.create_job_title(),
        }

    def create_new_name(self):
        num_names = random.choice([2, 2, 1])
        random_names = random.sample(self.local_names, num_names)
        mid_name = random.choice(self.mid_names)
        if num_names > 2:
            return (' ' + mid_name + ' ').join(random_names)
        return random_names[-1] + ' ' + mid_name

    def create_job_title(self):
        pass

    def extract_names_from_file(self):
        file_path = 'resources/African-Names.csv'
        names_file_df = pd.read_csv(file_path)
        random_plant_col = random.choice(['Orchids', 'Ferns'])
        names_series = names_file_df['African-names']
        all_plants_series = names_file_df[random_plant_col]
        valid_plants_series = all_plants_series.dropna()
        self.local_names = names_series.tolist()
        self.mid_names = valid_plants_series.tolist()


if __name__ == '__main__':
    main()
