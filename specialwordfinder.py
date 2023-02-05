# PATH = /Users/sethvargas/Desktop/Main/springboard/exercises/python-oo-practice/specialwords.txt

from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)

    def get_words(self, PATH):
        words = set()
        file = open(PATH, 'r')
        for line in file:
            if not line.startswith('#') and not line.startswith('\n'):
                words.add(line.rstrip('\n'))
        file.close()
        return list(words)