"""Word Finder: finds random words from a dictionary."""

# PATH = /Users/sethvargas/Desktop/Main/springboard/exercises/python-oo-practice/words.txt

from random import choice

class WordFinder:
    """
    Instantiated with a path to a file on disk that contains words, one word per line
    - reads that file, and makes an attribute of a list of those words
    - prints out “[num-of-words-read] words read”

    Provides a method, random(), which returns a random word from that list of words

    NOTE the random method should not re-read the list of words each time;
         it should work with the already-read-in list of words
    """

    def __init__(self, path):
        self.path = path
        self.words = self.get_words(self.path)
        print(f"{len(self.words)} words read")

    def get_words(self, PATH):
        words = set()
        file = open(PATH, 'r')
        for line in file:
            words.add(line)
        file.close()
        return list(words)

    def random(self):
        return choice(self.words)