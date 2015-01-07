from __future__ import division

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

# relative path of target data files about topic distribution
FBT_PATH = './frequency-based-topics.txt'
PBT_PATH = './probability-based-topics.txt'


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


class Calculator:

    def __init__(self, loader, writer):
        self.loader = loader
        self.writer = writer

    def iteration(self):
        groups = self.loader.corpus.groups

        for group in groups:
            prob_dist = {}
            freq_dist = []

            word_dict = self.loader.corpus.words[group]
            words = sorted(word_dict, key=word_dict.get)
            words.reverse()

            for word in words:
                prob_dist[word] = self.probability(word, group)
                freq_dist.append([word, word_dict[word]])

            self.writer.process(prob_dist, 'prob', group)
            self.writer.process(freq_dist, 'freq', group)

    def probability(self, word, group):
        corpus = self.loader.corpus.words
        groups = self.loader.corpus.groups

        num = corpus[group][word]
        den = 0

        # this is the **one should not use** way of doing this
        # can be done efficiently by pre-computing the word frequencies
        for group in groups:
            if word in corpus[group].keys():
                den += corpus[group][word]

        return num / den


class Writer:

    def __init__(self):
        self.fbt_file = os.path.join(os.path.dirname(__file__), FBT_PATH)
        self.pbt_file = os.path.join(os.path.dirname(__file__), PBT_PATH)

    def process(self, dictionary, section, group):
        if (section == 'freq'):
            self.write(section, "\n%s\n\n" % (group))

            for word_freq in dictionary:
                self.write(section, "%s : %s\n" % (word_freq[0], word_freq[1]))

        elif (section == 'prob'):
            self.write(section, "\n%s\n\n" % (group))

            sorted_dictionary = sorted(dictionary, key=dictionary.get)
            sorted_dictionary.reverse()

            for word in sorted_dictionary:
                self.write(section, "%s : %s\n" % (word, dictionary[word]))
            

    def write(self, section, string):
        filepath = self.fbt_file
        if (section == 'prob'):
            filepath = self.pbt_file

        with open(os.path.abspath(filepath), 'a') as writefile:
            writefile.write("%s" % (string))


corpus = Corpus(GROUP_FILE_PATH)

loader = Loader(SOURCE_FILE_PATH, corpus, Colander())
loader.read_data()

writer = Writer()
calc = Calculator(loader, writer)
calc.iteration()
