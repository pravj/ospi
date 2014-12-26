"""
utils.py
========

This module implements some utility functions to help the project.
"""

import datetime


def week_index(timestamp):
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    date = datetime.datetime.strptime(timestamp, fmt)

    return date.isocalendar()[1]
