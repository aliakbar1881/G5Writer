#from webscrap import request
class word:
    #def __init__(self, word, type_, phonetic):
    def __init__(self, word, type_):
        self.word = word
        self.type_ = type_
    def explain(self, explain):
        self.explain = explain
    def example(self, example):
        self.example = example
def main():
    word_dict =dict()
    _path = '../data/prepart.txt'
    with open(_path, 'r') as f :
        words = 0
        f = f.readlines()
        for i in f:
            line = str(i)
            if '(' in i:
                index = line.find('(')
                words = line[:index]
                type_= line[index:]
                #word_dict.update({words:word(words, type_, request(words))})
                word_dict.update({words:word(words, type_)})
            elif '|' in i:
                explain = line[1:]
                word_dict.get(words).explain(explain)
            elif all([i is None, ' ' in i]):
                continue

            else:
                example = line
                word_dict.get(words).example(example)
    return word_dict

if __name__ == '__main__':
    main()
    print('succsed')
