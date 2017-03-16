#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------

import numpy as np
from dictionary import Dictionary
from sklearn.cluster import KMeans

class WordCluster(object):
    """
    Clustering words by similarity
    """
    
    def __init__(self, mode='k-means',**kwargs):
        self.setMode(mode,**kwargs)
      
    def setMode(self, mode='k-means',**kwargs):
        if mode=='k-means':
            self.mode=mode
            if kwargs.has_key('k'):
                self.k=kwargs['k']
            else:
                self.k=2            
        else:
            self.mode='error'

            
    def cluster(self,queryResults,**kwargs):
         """
         cluster words by diffrent methods

         """
         if self.mode=='k-means':
            return self.clusterByKmeans(queryResults,**kwargs)
         else:
            print 'unknow cluster method'
            return []

    def clusterByKmeans(self,queryResults,**kwargs):
         """
         cluster words by k-means method

         """
         if self.mode!='k-means':
             print 'cluster mode is not k-means'
             return [queryResults[0]]

         words=queryResults[0]
         vecs=queryResults[1]
         X = np.array(vecs)
         if kwargs.has_key('k'):
             k=kwargs['k']
         else:
             k=self.k
         if k>len(words):
             k=len(words)
         kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        # print kmeans.labels_
         result=[]
         for i in xrange(k):
             result.append([])
         for i in xrange(len(words)):
             result[kmeans.labels_[i]].append(words[i])
         return result



    def clusterBySimilaritySort(self,queryResults):
         """
         cluster words by similarity sort method

         """
         #TODO:
         result =[words]
         pass
         return result

    def getSimilarity(self,vec1,vec2):
         """
         get similarity between two words

         """
         return np.dot(vec1,vec2)


if __name__ == '__main__':

    word='word'
    k=2
    testDic=Dictionary('dic.pkl')
    queryResults=testDic.query(word)
    wordClusters = WordCluster('k-means',k=k).cluster(queryResults)
    for c in wordClusters:
        print c
