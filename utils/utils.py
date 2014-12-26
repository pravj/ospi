"""
utils.py
========

This module implements some utility functions to help the project.
"""

import datetime


def week_index(date):
    return date.isocalendar()[1]

def creation_date(timestamp):
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    date = datetime.datetime.strptime(timestamp, fmt)

    return date
