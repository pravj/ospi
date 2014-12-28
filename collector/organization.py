# -*- coding: utf-8 -*-

"""
ospi/collector/organization.py
===============

This module handles obtaining and managing organization information.
"""

import os
import requests


class Organization:

    def __init__(self, name, postman):
        self.postman = postman

        self.name = name
        self.repos = 0
        self.members = 0
        self.created = None
        self.repo_list = []

        self.data_file = '../data/organizations.csv'

        self.postman.update(self.name)

    def write_data(self):
        data_string = "%s, %d, %d, %s\n" % (
            self.name, self.repos, self.members, self.created)

        file_path = os.path.join(os.path.dirname(__file__), self.data_file)

        with open(os.path.abspath(file_path), 'a') as f:
            f.write(data_string)

    def org_info(self):
        response = self.postman.request('info')

        if (response.status_code == requests.codes.ok):
            data = response.json()

            self.repos = data['public_repos']
            self.created = data['created_at']
            self.updated = data['updated_at']

            self.repo_info()
            self.member_info()

    def repo_info(self, attempt=1):
        response = self.postman.request('repo_list', page=attempt)

        if (response.status_code == requests.codes.ok):
            if (len(response.json()) != 0):
                for repo in response.json():
                    self.repo_list.append(repo['name'])

                self.repo_info(attempt=attempt + 1)

    def member_info(self, attempt=1):
        response = self.postman.request('member_list', page=attempt)

        if (response.status_code == requests.codes.ok):
            if (len(response.json()) != 0):
                self.members += len(response.json())

                self.member_info(attempt=attempt + 1)
