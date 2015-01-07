"""
ospi/classifier/classifier.py
=============================

This module implements a basic naive classifier model for repository descriptions.
"""

import os
import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

# relative path of source csv data file
SOURCE_FILE_PATH = '../data/repositories.csv'


class Colander:

    def __init__(self):
        # takes care of necessary '.' character; like the word 'angular.js'
        self.tokenizer = RegexpTokenizer(r'\w+(\.\w+)?')

        self.lemmatizer = WordNetLemmatizer()

    def process(self, sentence):
        # selects onlt alphanumeric words
        words = self.tokenizer.tokenize(sentence)

        # lemmatize the words
        words = [self.lemmatizer.lemmatize(word) for word in words]

        # lowercase all the words and remove single characters
        words = [word.lower() for word in words if len(word) > 1]

        # remove the stopwords using NLTK
        words = [word for word in words if word not in stopwords.words('english')]

        return words


class LoadCorpus:

    def __init__(self, source_file, colander):
        self.colander = colander
        self.source_file = os.path.join(os.path.dirname(__file__), source_file)

    def read_data(self):
        with open(os.path.abspath(self.source_file), 'rb') as csvfile:
            # read the row content accordint to particular columns
            reader = csv.DictReader(csvfile)

            for row in reader:
                words = colander.process("".join(row[' description'], row[' repository']))


lc = LoadCorpus(SOURCE_FILE_PATH)
lc.read_data()
