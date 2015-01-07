"""
ospi/classifier/colander.py
===========================

This module implements text filtering which uses NLTK in-builts.
It helps removing punctuation/stop words, lemmatization etc.
"""

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer


class Colander:

    def __init__(self):
        # takes care of necessary '.' character; like the word 'angular.js'
        self.tokenizer = RegexpTokenizer(r'[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?')

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
