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

def getSimilarity(words):
    #TODO:
    pass
    result=[[]]
    return result

if __name__ == '__main__':
    words=["act","action","activity","actual","actually"]
    print getSimilarity(words)
    model_google = gensim.models.KeyedVectors.load_word2vec_format(
        'GoogleNews-vectors-negative300.bin',
        binary=True)
    
    for i in words:
        print i+' ',
    print '\n'
    for i in words:
        print i,
        for j in words:
            print '%f'%similarity(i, j, model_google),
        print '\n'


