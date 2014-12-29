# -*- coding: utf-8 -*-

"""
ospi/collector/postman.py
==========

This module helps the data collection process by interacting with GitHub API.
"""

import os
import json
import time
import requests
from organization import Organization


class Linker:

    def __init__(self):
        self.org = None

    def info(self):
        """ Return URL instance for organization's information.
        """

        url = "https://api.github.com/orgs/%s" % (self.org)
        return url

    def repo_list(self):
        """ Return URL instance for repository list of an organization.
        """

        url = "https://api.github.com/orgs/%s/repos" % (self.org)
        return url

    def member_list(self):
        """ Return URL instance for members list of an organization.
        """

        url = "https://api.github.com/orgs/%s/public_members" % (self.org)
        return url

    def repo(self, name):
        """ Return URL instance for a particular repository.
        """

        url = "https://api.github.com/repos/%s/%s" % (self.org, name)
        return url

    def repo_languages(self, name):
        """ Return URL instance for a repository's language stats.
        """

        url = "https://api.github.com/repos/%s/%s/languages" % (self.org, name)
        return url

    def repo_stats(self, name):
        """ Return URL instance for a repository's commit activity.
        """

        url = "https://api.github.com/repos/%s/%s/stats/participation" % (
            self.org, name)
        return url


class Postman:

    def __init__(self):
        self.linker = Linker()
        self.token = None

        self.config_file = '../config/config.json'
        self.config_path = os.path.join(os.path.dirname(__file__), config_file)

        with open(os.path.abspath(self.config_path), 'r') as f:
            data = json.loads(f.read())
            self.token = data['access-token']

    def update(self, org):
        """ Update organization to look up for.
        """

        self.linker.org = org

    def address(self, *section, **kwargs):
        """ Return URL string according to particular section.
        """

        default_name = ''
        default_url = ''

        # use it for repository's name
        if 'name' in kwargs.keys():
            default_name = kwargs['name']

        # return explicit URL
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

        # pagination support
        if 'page' in kwargs.keys():
            url += "?page=%d" % (kwargs['page'])

        return url

    def request(self, *section, **kwargs):
        """ Return the response status.
        Takes care of data-not-yet-cached issue.
        """

        # use specified access token for authentication
        # After authentication one can make 5000 API requests per day.
        headers = {'Authorization': "token %s" % (self.token)}

        url = self.address(section[0], **kwargs)
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
