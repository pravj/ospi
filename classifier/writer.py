"""
ospi/classifier/writer.py
=========================

This module implements 'Writer' class.
Which helps storing the distribution result in respective files.
"""

import os

# relative path of target data files about topic distribution
FBT_PATH = '../results/frequency-based-topics.txt'
PBT_PATH = '../results/probability-based-topics.txt'


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
