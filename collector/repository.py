"""
ospi/collector/repository.py
=============

This module handels obtaining and managing repository information.
"""

import os
import requests


class Repository:

    def __init__(self, name, org):
        self.name = name
        self.org = org

        self.is_fork = 0
        self.stars = 0
        self.forks = 0
        self.language = None
        self.description = None
        self.created = None

        self.data_file = '../data/repositories.csv'

    def write_data(self):
        data_string = "%s, %s, %d, %s, %d, %d, %s, %s\n" % (
            self.org.name, self.name, self.is_fork, self.language, self.stars,
            self.forks, self.created, self.description)

        file_path = os.path.join(os.path.dirname(__file__), self.data_file)

        with open(os.path.abspath(file_path), 'a') as f:
            f.write(data_string)

    def repo_info(self):
        response = self.org.postman.request('repo', name=self.name)

        if (response.status_code == requests.codes.ok):
            data = response.json()

            self.is_fork = 1 if data['fork'] else 0
            self.stars = data['stargazers_count']
            self.forks = data['forks_count']
            self.language = data['language']
            self.description = data['description']
            self.created = data['created_at']
