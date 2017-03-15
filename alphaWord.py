#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------


from dictionary import Dictionary
from wordCluster import WordCluster


if __name__ == '__main__':
    testDic=Dictionary('dic.txt')
    testCluster=WordCluster('k-means')   
    words=testDic.query('act')
    result=testCluster.cluster(words)
    print result
