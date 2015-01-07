"""
ospi/classifier/classifier.py
=============================

This module implements a basic naive classifier model for repository descriptions.
"""

import os
import csv
import json


class Loader:
    """ Loader class reads the source data files and format the data for further use.
    """

    def __init__(self, source_file, corpus, colander):
        self.corpus = corpus
        self.colander = colander
        self.source_file = os.path.join(os.path.dirname(__file__), source_file)

    def read_data(self):
        """ read the csv data files accordingly
        """

        with open(os.path.abspath(self.source_file), 'rb') as csvfile:
            # read the row content accordint to particular columns
            reader = csv.DictReader(csvfile)

            for row in reader:
                wordlist = self.colander.process("".join([row[' description'], row[' repository']]))

                self.corpus.learn_words(wordlist, row['organization'])


class Corpus:
    """ Corpus class implements corpus object that contains words
    and facilities function to operate on the content.
    """

    def __init__(self, group_file):
        self.group_file = os.path.join(os.path.dirname(__file__), group_file)

        # contains information about each groups and its word counts
        self.groups = {}
        # contains information about each groups and its words
        self.words = {}

        self.learn_groups()

    def learn_groups(self):
        """ learn the total groups available
        """

        with open(os.path.abspath(self.group_file), 'r') as jsonfile:
            groups = json.loads(jsonfile.read())

        for group in groups:
            self.groups.setdefault(group['handle'].lower(), {})
            self.groups[group['handle'].lower()].setdefault('count', 0)

            self.words.setdefault(group['handle'].lower(), {})

    def learn_words(self, wordlist, group):
        """ learn the words for a particular group/organization
        """

        for word in wordlist:
            self.words[group].setdefault(word, 0)
            self.words[group][word] += 1

            self.groups[group]['count'] += 1
