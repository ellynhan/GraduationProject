#from pprint import pprint as print
from gensim.models.fasttext import FastText as FT_gensim
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import os

corpus_file = datapath('/Users/hanjaewon/폴더모음/학교생활/졸업과제/fasttextTest/text_training')

#model: Training architecture. Allowed values: cbow,skipgram (Default cbow)
model = FT_gensim(size=100)

# build the vocabulary
model.build_vocab(corpus_file=corpus_file)
##print(model.epochs) #=5 ,default value.

# train the model
model.train(
    corpus_file=corpus_file, epochs=model.epochs,
    total_examples=model.corpus_count, total_words=model.corpus_total_words
)
print(model)
##model.save("model") #model.save("model",separately=[])와 다른점이 뭔지 모르겠음


#print('경제' in model.wv.vocab) #vocab에 단어가 있으면 True
#print(model.wv.__getitem__('경제')) #경제 단어의 vector값을 보여줌
#print('경기' in model.wv.vocab)
#print(model['경기']) #DeprecationWarning
print(model.wv.similarity("경제", "경기")) #두 단어의 유사도를 출력함
#print(model.wv.most_similar("경제"))
for v in model.wv.most_similar("경제"):
    print(v)

