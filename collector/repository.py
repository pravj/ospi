"""
repository.py
=============

This module handels obtaining and managing repository information.
"""

import os
import requests


class Repository:

    def __init__(self, name, org):
        self.name = name
        self.org = org

        self.is_fork = False
        self.stars = 0
        self.forks = 0
        self.language = None
        self.description = None

    def write_data(self):
        data_string = "%s, %s, %s, %s, %d, %d" % (self.name, self.org.name, self.is_fork, self.language, self.stars, self.forks)

        with open() as f:
            f.write(data_string)

    def repo_info(self):
        response = self.org.postman.request('repo', self.name)

        if (response.status_code == requests.codes.ok):
            data = response.json()

            self.is_fork = data['fork']
            self.stars = data['stargazers_count']
            self.forks = data['forks_count']
            self.language = data['language']
            self.description = data['description']
