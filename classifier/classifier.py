"""
ospi/classifier/classifier.py
=============================

This module implements a basic naive classifier model for repository descriptions.
"""

import os
import csv
import json
from colander import Colander

# relative path of source csv data file
SOURCE_FILE_PATH = '../data/repositories.csv'

# relative path of source json data file for groups/organizations
GROUP_FILE_PATH = '../config/organizations.json'


class Loader:

    def __init__(self, source_file, corpus, colander):
        self.corpus = corpus
        self.colander = colander
        self.source_file = os.path.join(os.path.dirname(__file__), source_file)

    def read_data(self):
        with open(os.path.abspath(self.source_file), 'rb') as csvfile:
            # read the row content accordint to particular columns
            reader = csv.DictReader(csvfile)

            for row in reader:
                wordlist = self.colander.process("".join([row[' description'], row[' repository']]))

                self.corpus.read_words(wordlist, row['organization'])


class Corpus:

    def __init__(self, group_file):
        self.group_file = os.path.join(os.path.dirname(__file__), group_file)

        self.groups = {}
        self.words = {}

        self.read_groups()

    def read_groups(self):
        with open(os.path.abspath(self.group_file), 'r') as jsonfile:
            groups = json.loads(jsonfile.read())

        for group in groups:
            self.groups.setdefault(group['handle'].lower(), {})
            self.groups[group['handle'].lower()].setdefault('count', 0)

            self.words.setdefault(group['handle'].lower(), {})

    def read_words(self, wordlist, group):
        for word in wordlist:
            self.words[group].setdefault(word, 0)
            self.words[group][word] += 1

            self.groups[group]['count'] += 1

        print self.words


corpus = Corpus(GROUP_FILE_PATH)

loader = Loader(SOURCE_FILE_PATH, corpus, Colander())
loader.read_data()
print loader.corpus.words
