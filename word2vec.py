import numpy as np
import gensim


# def buildWordVector(model_w2v, text, size):
#     sen = []
#     vec = np.zeros(size).reshape((1, size))
#     for word in text:
#         try:
#             vec = model_w2v[word].reshape((1, size))
#             sen.extend(vec)
#         except:
#             continue
#     return sen


def transform(word, model):
    n_dim = 300
    vector = model[word].reshape((1, n_dim))
    return vector


word = "action"
model_google = gensim.models.Word2Vec.load_word2vec_format(
    '../GoogleNews-vectors-negative300.bin',
    binary=True)
vector = transform(word, model_google)
print vector[0]
