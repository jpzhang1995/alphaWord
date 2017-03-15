#!/usr/bin/env python

# --------------------------------------------------------
# alphaWord
# Written by Junpeng Zhang
# --------------------------------------------------------


import os
import re



if __name__ == '__main__':
    testDic=Dictionary('dic.txt')
    result=testDic.query('act')
    print result
