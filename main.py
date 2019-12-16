# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:55:52 2019

@author: zyb32
"""

import os
import time
import re
from constants import *
from listening import AudioRecord,AipRecognize
from word import KeyWord
from preProcess import *
from get_code import getExpress,getLoop,getClass,getFunc,getLogic

    
    
def PIVmain(time):
    global N_indent
    N_indent = 0
    code_list = []
    last_text = ""      
    
    while True:
        AudioRecord(filepath0+"audio.pcm",time)
        try:
            origin_text = AipRecognize(filepath0+"audio.pcm")[0]   
        except IndexError:
            print("Nothing detected,please try again.(Use \'quit\' to stop dictation)\n")
            continue
        splited_text = origin_text.split()
        WordList = SegmentWords(splited_text)
        ########
        for x in WordList:
            print(x.name,x.type)
        ########
        head = WordList[0]
        same_text = False
        if head.type=="CMD":
            if head.name=="quit":
                return
            if head.name=="next":
                origin_text = last_text + " " + origin_text
                if (not origin_text) or (origin_text=="next"):
                    continue
                splited_text = origin_text.split()
                splited_text.remove("next")
                WordList = SegmentWords(splited_text)
                head = WordList[0]
                code_list.pop()
                same_text = True
            if head.name=="no":
                code_list.pop()
                
        if head.type=="KEY":
            if head.name=="slap":
                N_indent -= 1
            if head.name=="loop":
                code_list.append(getLoop(WordList))
                if not same_text:
                    N_indent += 1
            if head.name=="function":
                code_list.append(getFunc(WordList))
                if not same_text:
                    N_indent += 1
            if head.name=="class":
                code_list.append(getClass(WordList))
                if not same_text:
                    N_indent += 1
            if head.name=="expression":
                code_list.append(getExpress(WordList))
            if head.name=="if" or head.name=="else":
                code_list.append(getLogic(WordList))
                N_indent += 1
            if head.name=="break" or head.name=="continue" or head.name=="pass":
                code_list.append(head.name)
                N_indent -= 1
                
            code_list[-1] += ("\n"+"\t"*N_indent)
        last_text = origin_text
        #code = getCode(code_list)
        yield code_list












