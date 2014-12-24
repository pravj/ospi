"""
postman.py
==========

This module helps the data collection process by interacting with GitHub API.
"""

import requests


class Linker:

    def __init__(self):
        self.org = None

    def info(self):
        url = "https://api.github.com/orgs/%s" % (self.org)
        return url

    def repo_list(self):
        url = "https://api.github.com/orgs/%s/repos" % (self.org)
        return url

    def member_list(self):
        url = "https://api.github.com/orgs/%s/public_members" % (self.org)
        return url

    def repo(self, name):
        url = "https://api.github.com/repos/%s/%s" % (self.org, name)
        return url

    def languages(self, name):
        url = "https://api.github.com/repos/%s/%s/languages" % (self.org, name)
        return url

    def stats(self, name):
        url = "https://api.github.com/repos/%s/%s/stats/participation" % (self.org, name)


class Postman:

    def __init__(self):
        pass
