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
        """ process the provided data and write it to respective storage file
        """

        self.write(section, "\n%s\n\n" % (group))

        if (section == 'freq'):
            for word_freq in dictionary:
                self.write(section, "{0} : {1}\n".format(word_freq[0], word_freq[1]))

        elif (section == 'prob'):
            sorted_dictionary = sorted(dictionary, key=dictionary.get)
            sorted_dictionary.reverse()

            for word in sorted_dictionary:
                self.write(section, "{0} : {1}\n".format(word, dictionary[word]))
            

    def write(self, section, string):
        """ write a string to a particular storage file accordingly
        """

        filepath = self.pbt_file if section == 'prob' else self.fbt_file

        with open(os.path.abspath(filepath), 'a') as writefile:
            writefile.write("%s" % (string))
