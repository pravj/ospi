from __future__ import division

"""
ospi/classifier/calculator.py
=============================

This module helps calculating the word frequencies.
It also implements conditional probabilities using Baye's theorm.
"""


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
