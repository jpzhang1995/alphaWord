#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------


import os
import re
import traceback
import cPickle as pickle  

class Dictionary(object):
    """
    a dictionary
    """
    
    def __init__(self, dicPath='dic.pkl'):
        self.wordList=[]
        self.embDic={}
        if  not os.path.exists(dicPath):
            print dicPath+' not exist.'
            return            
        try:
            dicFile = open(dicPath,'rb') 
            obj = pickle.load(dicFile)
            self.wordList=obj[0]
            self.embDic=obj[1]
        except:
            print 'can not load '+dicPath
            traceback.print_exc()     
        finally:
            dicFile.close( )
            
    def query(self,prefix):
         """
         query all words with  a given prefix from a  word dictionary

         """
         result =[ [ ] , [ ] ]

         p1='^'+prefix+r'[a-zA-Z]*$'
         pattern = re.compile(p1) 
         for word in self.wordList:
             if pattern.match(word):
                 result[0].append(word)
                 result[1].append(self.embDic[word])
         return result


if __name__ == '__main__':
    testDic=Dictionary('dic.pkl')
    result=testDic.query('act')
    print result[0]
 #   print result[1][0]
