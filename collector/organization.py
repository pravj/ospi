# -*- coding: utf-8 -*-

"""
organization.py
===============

This module handles obtaining and managing organization information.
"""

import os
import requests


class Organization:

    def __init__(self, name, postman):
        self.postman = postman

        self.name = name
        self.repos = None
        self.members = None
        self.created = None
        self.updated = None
        self.repo_list = []

        postman.update(self.name)

    def write_data(self):
        data_string = "%s, %d, %d, %s, %s" % (
            self.name, self.repos, self.members, self.created, self.updated)

        with open() as f:
            f.write(data_string)

    def org_info(self):
        response = postman.request('info')

        if (response.status_code == requests.codes_ok):
            data = response.json()

            self.repos = data['public_repos']
            self.created = data['created_at']
            self.updated = data['updated_at']

            self.repo_info()
            self.members_info()

    def repo_info(self):
        response = postman.request('repo_list')

        if (response.status_code == requests.codes_ok):
            pass
