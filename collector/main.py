"""
ospi/collector/main.py
======================

This module integrate all the modules and collect the data.
"""

import os


data_files = ['../data/organizations.csv', '../data/repositories.csv',
              '../data/timeline.csv', '../data/forked_repo_stats.csv']
headers = []


def add_headers():
    for i in range(len(headers)):
        file_path = os.path.join(os.path.dirname(__file__), data_files[i])

        with open(os.path.abspath(file_path), 'w') as f:
            f.write(headers[i])


def generate_headers():
    # organizations.csv
    headers.append("organization, public_repos, public_members, created_at")

    # repositories.csv
    headers.append("organization, repository, is_fork, language, stars, forks")

    # timeline.csv
    week_label = ", ".join(["week_%d" % (i + 1) for i in range(52)])
    headers.append("organization, repository, %s" % (week_label))

    # forked_repo_stats.csv
    headers.append("organization, repository, commits")
