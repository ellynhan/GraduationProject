from gensim.models import Word2Vec as W2V_gensim
from gensim.test.utils import datapath
from gensim.models import KeyedVectors

corpus_file=datapath('/Users/hanjaewon/폴더모음/학교생활/졸업과제/word2vecTest/text_training')
model = W2V_gensim(min_count=5)
model.build_vocab(corpus_file = corpus_file)
model.train(
    corpus_file=corpus_file, epochs=model.epochs,
    total_examples=model.corpus_count, total_words=model.corpus_total_words
)
#print('경제' in model.wv.vocab)
#print(model.wv.__getitem__('경제'))
print(model.wv.similarity("경제","경기"))
for v in model.wv.most_similar("경제"):
    print(v)
