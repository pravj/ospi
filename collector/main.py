"""
ospi/collector/main.py
======================

This module integrate all the modules and collect the data.
"""

import os
import json
import time
from postman import Postman
from organization import Organization
from repository import Repository
from timeline import Timeline


# data store files
data_files = ['../data/organizations.csv', '../data/repositories.csv',
              '../data/timeline.csv', '../data/forked_repo_stats.csv']
# headers for each data store file
headers = []


def add_headers():
    """ Add header row in all the data files. It has column names.
    """

    for i in range(len(headers)):
        file_path = os.path.join(os.path.dirname(__file__), data_files[i])

        with open(os.path.abspath(file_path), 'w') as f:
            f.write(headers[i])


def generate_headers():
    """ Generate the header row for each data file.
    """

    # organizations.csv
    headers.append("organization, public_repos, public_members, created_at\n")

    # repositories.csv
    headers.append("organization, repository, is_fork, language, stars, forks, created_at, description\n")

    # timeline.csv
    week_label = ", ".join(["week_%d" % (i + 1) for i in range(52)])
    headers.append("organization, repository, %s\n" % (week_label))

    # forked_repo_stats.csv
    headers.append("organization, repository, commits\n")


def collect():
    """ Collect the data for each organization and process it.
    """

    orgs_file = os.path.join(
        os.path.dirname(__file__), '../config/organizations.json')
    with open(os.path.abspath(orgs_file), 'r') as f:
        orgs = json.loads(f.read())

    # postman.Postman instance for interacting with GitHub API
    postman = Postman()

    # iterating over all the organizations
    for org in orgs:
        print "collecting data for %s" % (org['handle'])
        organization = Organization(org['handle'], postman)
        organization.org_info()
        organization.write_data()

        for repo in organization.repo_list:
            print "collecting data for repo %s/%s" % (org['handle'], repo)
            repository = Repository(repo, organization)
            repository.repo_info()
            repository.write_data()

            print "collecting data for repo %s/%s's timeline" % (org['handle'], repo)
            timeline = Timeline(
                repo, organization, repository.created, repository.is_fork)
            timeline.timeline_info()
            timeline.write_data()

        # wait for a minute after completing an organization
        # step to mitigate API rate-limiting issue, if any
        time.sleep(60)


if __name__ == "__main__":
    generate_headers()
    add_headers()
    collect()
