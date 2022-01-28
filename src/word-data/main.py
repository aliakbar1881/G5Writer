"""
    Script
"""

from pathlib import Path

from src.IO import IO_DIR as DATA
from src.utils.docing import doc_gen
from src.utils.webscrap import word_request

class Main:

    def __init__(self, words_File):
        path = Path(DATA / words_File)
        self.word_gr_name = path.stem
        self.words_gene(path)

    def words_gene(self, path):
        words_dict = dict()
        with open(path, 'r') as f_o:
            my_iter = map(lambda items: items.strip(), f_o)
            count = 0
            f_o = next(my_iter)
            while str(f_o) != 'end':
                words_dict.update({f_o:self.WordsClass(f_o)})
                word = words_dict[f_o]
                type_ = next(my_iter)
                explain = next(my_iter)
                example = next(my_iter)
                word.word_gener(type_, explain, example)
                count += 1
                f_o = next(my_iter)
        self.words_dict = words_dict
        self.count = count

    class WordsClass:

        def __init__(self, word):
            self.word = word
            self.type_ = None
            self.example = None
            self.explain = None
            self.phonetic = None

        def word_gener(self, type_, explain, example):
            self.type_ = type_
            self.explain = explain
            self.example = example

        def word_phonetic(self):
            self.phonetic = word_request(self.word)

    def docing(self):
        words = self.words_dict
        doc_gen(words, self.word_gr_name)

if __name__ == '__main__':
    text_file = input('Please insert your text file : ')
    my_words = Main(text_file).docing()
