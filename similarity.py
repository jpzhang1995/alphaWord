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


def similarity(word1, word2, model):
    value = model.similarity(word1, word2)
    return value


def getSimilarity(word1, word2):
    #TODO:
    pass
    value=1
    return value



if __name__ == '__main__':
    word1 = "action"
    word2 = "activity"
    model_google = gensim.models.Word2Vec.load_word2vec_format(
        '../GoogleNews-vectors-negative300.bin',
        binary=True)
    simi = similarity(word1, word2, model_google)
    print simi
