# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:43:16 2019

@author: zyb32
"""
import numpy as np
from math import sqrt,inf
from constants import *
from word import KeyWord

def calcCosDist(LetDict1,LetDict2):
    unique_letr_dict = LetDict1.copy()
    unique_letr_dict.update(LetDict2)
    unique_letr_list = list(unique_letr_dict.keys())
    num = len(unique_letr_list)
    Vec1 = unique_letr_dict.copy()
    Vec2 = unique_letr_dict.copy()
    for i in range(len(unique_letr_list)):
        ele = unique_letr_list[i]
        if ele in LetDict1:
            Vec1[ele] = LetDict1[ele]
        else:
            Vec1[ele] = 0
            
        if ele in LetDict2:
            Vec2[ele] = LetDict2[ele]
        else:
            Vec2[ele] = 0
    
    Vec1 = list(Vec1.values())
    Vec2 = list(Vec2.values())
    dist = 0
    for i in range(num):
        dist += (Vec1[i]*Vec2[i])
        Vec1[i] = Vec1[i]**2
        Vec2[i] = Vec2[i]**2
    try:
        dist /= (sqrt(sum(Vec1))*sqrt(sum(Vec2)))
    except ZeroDivisionError:
        dist = 0
    return dist
    
def calcSeqFactor(str1,str2):
    max_num = max(len(str1),len(str2))
    weights = np.linspace(1,0.8,num=max_num)
    res = 0
    count = 0
    for i in range(max_num):
        try:
            if str1[i]==str2[i]:
                res += (weights[i]*1)
                count += 1
            else:
                res += (1-weights[i])*1
        except IndexError:
            continue
    return res/(max_num-count)
    


def DistanceList(word,lst):
    if not lst:
        return 
    res = []
    LetterDict = {}
    for letr in word:
        if not (letr in LetterDict.keys()):
            LetterDict.setdefault(letr,1)
        else:
            LetterDict[letr] += 1
            
    for i in range(len(lst)):
        cmp_word = lst[i]
        cmpLetterDict = {}
        for letr in cmp_word:
            if not (letr in cmpLetterDict.keys()):
                cmpLetterDict.setdefault(letr,1)
            else:
                cmpLetterDict[letr] += 1
        cosDist = calcCosDist(LetterDict,cmpLetterDict)
        seqFactor = calcSeqFactor(word,cmp_word)
        res.append(cosDist*seqFactor)
    return res
                
                

def SegmentWords(wordlist,threshold=0.8):
    res = []
    ArgList = []
    for word in wordlist:
        if word in KeyWordList:
            keyword = KeyWord(word,"KEY")
            res.append(keyword)
            continue
        if word in NumberWordList:
            keyword = KeyWord(word,"NUM")
            res.append(keyword)
            continue
        if word in ArgList:
            keyword = KeyWord(word,"ARG")
            res.append(keyword)
            continue
        if word in OpList:
            keyword = KeyWord(word,"OPR")
            res.append(keyword)
            continue
        if word in CmdList:
            keyword = KeyWord(word,"CMD")
            res.append(keyword)
            continue
        CosDistList_Key = DistanceList(word,KeyWordList)
        CosDistList_Num = DistanceList(word,NumberWordList)
        if ArgList:
            CosDistList_Arg = DistanceList(word,ArgList)
            maxValList = [max(CosDistList_Key),max(CosDistList_Num),max(CosDistList_Arg)]
        else:
            maxValList = [max(CosDistList_Key),max(CosDistList_Num)]
        max_val = max(maxValList)
        max_idx = maxValList.index(max_val)
        if max_val<threshold:
            ArgList.append(word)
            keyword = KeyWord(word,"ARG")          
            res.append(keyword)
            continue
        else:
            if max_idx==0:
                keyword = KeyWord(KeyWordList[CosDistList_Key.index(max_val)],"KEY")
                res.append(keyword)
                continue
            if max_idx==1:
                keyword = KeyWord(NumberWordList[CosDistList_Num.index(max_val)],"NUM")
                res.append(keyword)
                continue
            if max_idx==2:
                keyword = KeyWord(ArgList[CosDistList_Arg.index(max_val)],"ARG")
                res.append(keyword)
                continue
    return res