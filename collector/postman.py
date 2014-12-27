# -*- coding: utf-8 -*-

"""
ospi/collector/postman.py
==========

This module helps the data collection process by interacting with GitHub API.
"""

import requests
from organization import Organization


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

    def repo_languages(self, name):
        url = "https://api.github.com/repos/%s/%s/languages" % (self.org, name)
        return url

    def repo_stats(self, name):
        url = "https://api.github.com/repos/%s/%s/stats/participation" % (self.org, name)
        return url


class Postman:

    def __init__(self):
        self.linker = Linker()

    def update(self, org):
        self.linker.org = org

    def address(self, section, **kwargs):
        default_name = ''
        default_url = ''

        if 'name' in kwargs.keys():
            default_name = kwargs['name']

        if 'url' in kwargs.keys():
            default_url = kwargs['url']

        url = {
            'info': self.linker.info(),
            'repo_list': self.linker.repo_list(),
            'member_list': self.linker.member_list(),
            'repo': self.linker.repo(default_name),
            'repo_languages': self.linker.repo_languages(default_name),
            'repo_stats': self.linker.repo_stats(default_name),
            'url': default_url
        }.get(section)

        if 'page' in kwargs.keys():
            url += "?page=%d" % (kwargs['page'])

        return url

    def request(self, section, **kwargs):
        url = self.address(section, **kwargs)
        response = requests.get(url)

        # return 'requests.models.Response' object
        if (response.status_code == requests.codes.ok):
            return response
        # the response data hasn't been cached, waiting a little
        elif (response.status_code == requests.codes.accepted):
            time.sleep(3)
            return self.request(url)
        # none of the favorable case
        else:
            print "Missed URL : %s" % (url)
            return response
