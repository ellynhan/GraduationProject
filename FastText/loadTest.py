from gensim.models.fasttext import FastText as FT_gensim

loaded_model = FT_gensim.load("model")
#print(loaded_model)
print(loaded_model.wv.vocab)
