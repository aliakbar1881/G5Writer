import src.phonetic as ph

class words:
    def __init__(self, word, Type, phonetic):
        self.Type = Type
        self.phonetic = phonetic

    def explaination(self, explain):
        self.explain = explain

    def example(self, example):
        self.example = example

vocab_list = list() 
with open('part.txt') as part:
    line = part.readlines()
    for i in line:
        if '(' in i :
            i = i.strip()
            g = i.find('(')
            word = i[:g]
            Type = i[g:]
            vocab_list.append(words(word, Type, ph.phonetic(word)))
            print(vocab_list[-1].Type)
        elif i[0].isupper() :
            i = i[:-2]
            vocab_list[-1].example(i)

        else:
            vocab_list[-1].explaination(i)
print('success')



    
