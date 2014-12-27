"""
timeline.py
===========

This module handles obtaining and managing organization's timeline stats.
"""

import requests
from utils import creation_date, week_index


class Timeline:

    def __init__(self, name, org, created, is_fork):
        self.name = name
        self.org = org
        self.is_fork = is_fork

        self.created = created
        self.week_count = [0 for i in range(52)]

        self.data_file_t = '../data/timeline.csv'
        self.data_file_f = '../data/forked_repo_stats.csv'

    def write_data(self):
        data_string = "%s, %s, %s\n" % (
            self.org.name, self.name, ", ".join([str(wc) for wc in self.week_count]))

        t_file_path = os.path.join(os.path.dirname(__file__), self.data_file_t)

        with open(os.path.abspath(t_file_path), 'w') as f:
            f.write(data_string)

        if (self.is_fork):
            data_string = "%s, %s, %d\n" % (
                self.org.name, self.name, self.fork_info())

            f_file_path = os.path.join(
                os.path.dirname(__file__), self.data_file_f)

            with open(os.path.abspath(f_file_path), 'w') as f:
                f.write(data_string)

    def filter_activity(self):
        index = 0
        date = creation_date(self.created)

        if (date.year == 2014):
            week_index = week_index(date)
            index = week_index
        else:
            pass

        return index

    def timeline_info(self):
        response = self.org.postman.request('repo_stats')

        if (response.status_code == requests.codes.ok):
            data = response.json()
            commits = data['all']

            if (self.is_fork):
                index = self.filter_activity(commits)

                for i in range(index, 52):
                    self.week_count[i] = commits[i]
            else:
                self.week_count = [commit for commit in commits]

    def fork_info(self):
        return sum(self.week_count)
