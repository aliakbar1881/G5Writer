"""
    Main Script
"""

from pathlib import Path
from collections import defaultdict, Counter
from loguru import logger

from src.IO import IO_DIR as DATA
from src.utils.documenter import doc_gen
from src.utils.webscrap import word_phonetic

class Main:

    def __init__(self, words_file):
        path = Path(DATA / words_file)
        self.word_file_name = path.stem
        self.word_list = dict()
        self.words_data_generator(path)
        self.amount = sum(Counter(self.word_list.keys()).values())

    def __str__(self):
        logger.info('Some data about your proccesing.')
        print('\n'*4)
        logger.info('List of words')
        print(self.word_list.keys())
        print('\n'*2)
        logger.info('Number of words.')
        print(self.amount)
        print('\n'*2)
        logger.info('File name :')
        print(self.word_file_name)
        return '===========Done!==========='

    def words_data_generator(self, path):
        with open(path, 'r') as f_o:
            my_iter = map(lambda items: items.strip(), f_o)
            word = next(my_iter)
            while word:
                self.word_list.update({word:defaultdict(lambda: "None")})
                this_word = self.word_list[word]
                this_word['type_'] = next(my_iter)
                this_word['explain'] = next(my_iter)
                this_word['example'] = next(my_iter)
                this_word['phonetic'] = word_phonetic(word)
                #  this_word[p_speech] = word_p_speech()
                word = next(my_iter)


    def docing(self):
        doc_gen(self.word_list, self.word_file_name)

if __name__ == '__main__':
    text_file = input('Please insert your text file : ')
    my_words = Main(text_file)
    print(my_words)
    logger.info('Writing on Document...')
    my_words.docing()
    logger.success('No Error......')
