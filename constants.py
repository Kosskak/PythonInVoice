# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:28:19 2019

@author: zyb32
"""

APP_ID = "17607733"
API_KEY = "WFkyjUHUoiYvFSKHK9sWN2kW"
SECRET_KEY = "E4wMVFtIvvT0SXseiHtGEVKGCwms5ugq"
#filename = "test.wav"
filepath0 = r"Audio//"
KeyWordList = [
               "slap",
               "loop",
               "in",
               "from",
               "to",
               "step",
               "break",
               "continue",
               "none",
               "function",
               "class",
               "if",
               "else",
               "pass",
               "argument",
               "expression",
               ]
OpList = ["bracket","plus","minus","multiply","devide","attribute",
          "bigger","smaller","index","and","or","not","is","return"]

OpDict = {"plus":"+","minus":"-","multiply":"*","devide":"/",
          "attribute":".","return":"return ","bigger":">","smaller":"<"}

CmdList = ["quit","next","no"]

WordToNumber = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0,"ten":10}
NumberWordList = list(WordToNumber.keys())



























