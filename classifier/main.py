from calculator import Calculator
from classifier import Corpus, Loader
from colander import Colander
from writer import Writer

# relative path of source csv data file
SOURCE_FILE_PATH = '../data/repositories.csv'

# relative path of source json data file for groups/organizations
GROUP_FILE_PATH = '../config/organizations.json'


if __name__ == '__main__':

    # text corpus
    corpus = Corpus(GROUP_FILE_PATH)

    # populate the corpus
    loader = Loader(SOURCE_FILE_PATH, corpus, Colander())
    loader.read_data()

    writer = Writer()

    # calculate and write distribution results
    calculator = Calculator(loader, writer)
    calculator.iteration()
