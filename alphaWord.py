#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------


from dictionary import Dictionary
from wordCluster import WordCluster


if __name__ == '__main__':
    
    word='com'
    k=10
    
    testDic=Dictionary('dic.pkl')
    testCluster=WordCluster('k-means',k=k)
    results=testDic.query(word)  
    wordClusters=testCluster.cluster(results)
    for c in wordClusters:
        print c
        print '\n'
