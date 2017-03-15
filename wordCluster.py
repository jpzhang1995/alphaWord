#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------

from dictionary import Dictionary
from similarity import getSimilarity

class WordCluster(object):
    """
    Clustering words by similarity
    """
    
    def __init__(self, mode='k-means'):
        if mode=='k-means':
            self.mode=mode
        else:
            self.mode='error'
      
            
    def cluster(self,words):
         """
         cluster words by diffrent methods

         """
         if self.mode=='k-means':
            return self.clusterByKmeans(words)
         else:
            print 'unknow cluster method'
            return []

    def clusterByKmeans(self,words):
         """
         cluster words by k-means method

         """
         #TODO:

         ############TEST###########
         result =[words]
         print getSimilarity(words[0],words[1])
         pass

         return result


if __name__ == '__main__':
    testDic=Dictionary('dic.txt')
    words=testDic.query('act')
    result = WordCluster('k-means').cluster(words)
    print result
