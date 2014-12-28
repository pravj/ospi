# -*- coding: utf-8 -*-

"""
ospi/collector/postman.py
==========

This module helps the data collection process by interacting with GitHub API.
"""

from organization import Organization
import requests
import time


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
        url = "https://api.github.com/repos/%s/%s/stats/participation" % (
            self.org, name)
        return url


class Postman:

    def __init__(self):
        self.linker = Linker()

    def update(self, org):
        self.linker.org = org

    def address(self, *section, **kwargs):
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
        }.get(section[0])

        if 'page' in kwargs.keys():
            url += "?page=%d" % (kwargs['page'])

        return url

    def request(self, *section, **kwargs):
        url = self.address(section[0], **kwargs)
        headers = {
            'Authorization': 'token 84e87ee5d747b9f1de549c165df2d3ab9c4c339c'}
        response = requests.get(url, headers=headers)

        # return 'requests.models.Response' object
        if (response.status_code == requests.codes.ok):
            return response
        # the response data hasn't been cached, waiting a little
        elif (response.status_code == requests.codes.accepted):
            print "Retrying for %s" % (url)
            time.sleep(5)
            return self.request(*section, **kwargs)
        # none of the favorable case
        else:
            print "Missed URL : %s" % (url)
            return response
