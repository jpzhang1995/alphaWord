#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------


import os
import re


class Dictionary(object):
    """
    a dictionary
    """
    
    def __init__(self, dicPath='dic.txt'):
        self.wordList=[]
        if  not os.path.exists(dicPath):
            print 'can not open '+dicPath
            return
        dicFile = open(dicPath,'r')      
        try:
            for line in dicFile:
                #print line
                line=line.strip('\n')
                self.wordList.append(line)              
        except:
            print 'can not read word list'
            
        finally:
            dicFile.close( )
            
    def query(self,prefix):
         """
         query all words with  a given prefix from a  word dictionary

         """
         result =[]

         p1='^'+prefix+r'\S*$'
         pattern = re.compile(p1) 
         for word in self.wordList:
             if pattern.match(word):
                 result.append(word)
         return result


if __name__ == '__main__':
    testDic=Dictionary('dic.txt')
    result=testDic.query('act')
    print result
