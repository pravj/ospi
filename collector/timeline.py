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
        self.fork_work = 0

    def write_data(self):
        with open() as f:
            f.write()

        if (self.is_fork):
            self.fork_work = self.fork_info()

            with open() as f:
                f.write()

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
