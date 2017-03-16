import numpy as np
import gensim
import os
import re
import traceback
import cPickle as pickle


class Word2Vec(object):
    
    def __init__(self,modelPath='GoogleNews-vectors-negative300.bin'):
        self.model=gensim.models.KeyedVectors.load_word2vec_format(
        'GoogleNews-vectors-negative300.bin',
        binary=True)

    def transform(self,word):
        n_dim = 300
        vector = self.model[word].reshape((1, n_dim))
        return vector


    def generateDic(self,dicPath, embWordsPath,picklePath):
        if not  os.path.exists(dicPath):
            print 'can not open '+dicPath
            exit(0)
            
        try:
            dicFile = open(dicPath,'r')
            embedFile=open(embWordsPath,'w')
            pickleFile=open(picklePath,'wb')
            
            p1=r'^[a-zA-Z]+$'
            pattern = re.compile(p1)
            embedDic={}
            wordList=[]
            for word in dicFile:
                #print line
                word=word.strip('\n')
                if pattern.match(word):
                    try:
                        vector = self.transform(word)
                        #print vector[0]
                        embedFile.write(word+'\n')
                        embedDic[word]=vector[0]
                        wordList.append(word)
                    except:
                        print  'word '+ word+' embedding failed'
                        
            pickle.dump([wordList,embedDic],pickleFile,True) 
            print 'word embedding successful'
        except:
            print 'word embedding failed'
            traceback.print_exc()
            
        finally:
            dicFile.close( )
            embedFile.close( )
            pickleFile.close( )



if __name__ == '__main__':
    w2v=Word2Vec( 'GoogleNews-vectors-negative300.bin')
    print w2v.transform('action')
    
    #dicPath = 'raw.txt'
    #embWordsPath='wordList.txt'
    #picklePath='dic.pkl'
    #w2v.generateDic(dicPath, embWordsPath,picklePath)
    



