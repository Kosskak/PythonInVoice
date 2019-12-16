# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:45:33 2019

@author: zyb32
"""
from constants import *
from word import KeyWord
from listening import AudioRecord,AipRecognize

global N_indent

def getCode(lst):
    code = ""
    for c in lst:
        code += c
    return code
            
def getLoop(lst):
    global N_indent
    args = []
    nums = []
    keys = []
    loop_code = ""
    namelist = []
    for word in lst:
        namelist.append(word.name)
        if word.name == "slap":
            break
        elif word.type == "KEY":
            keys.append(word.name)
        elif word.type == "ARG":
            args.append(word.name)
        elif word.type == "NUM":
            nums.append(word.name)
        arg = args[0]
        
    loop_code = "for " + arg + " in range" + "("
    if len(nums) == 2:
        loop_code += (str(WordToNumber[nums[0]])+","+str(WordToNumber[nums[1]])) 
        
    if len(nums) == 3 and ("step" in namelist):
        loop_code += (str(WordToNumber[nums[0]])+","+str(WordToNumber[nums[1]])+","+str(WordToNumber[nums[2]]))
    
    loop_code += "):"
    return loop_code
        
def getFunc(lst):
    global N_indent
    args = []
    keys = []
    def_code = ""
    namelist = []
    for i in range(len(lst)):
        word = lst[i]
        namelist.append(word.name)
        if word.type == "KEY":
            if word.name == "for":
                word = KeyWord("four","NUM")
            elif word.name=="to":
                word = KeyWord("two","NUM")
            else:
                keys.append(word.name)
        if word.type == "ARG":
            if word.name=="south":
                word = KeyWord("self","ARG")
            if word.name=="egg" or word.name=="eggs" or word.name=="acts" or word.name=="ask": 
                word.name = "x"
            if word.name=="why":
                word.name = "y"
            args.append(word.name)

        if word.type == "NUM":
            if lst[i-1].type == "ARG":
                args[len(args)-1] += str(WordToNumber[word.name])
    
    def_code += "def "
    if not args:
        print("\nMissing function name.\nPlease add: ")
        AudioRecord("getfuncname.pcm",4)
        func_name = AipRecognize("getfuncname.pcm")[0]
        
    func_name = args.pop(0)
    if func_name == "initiate":
        func_name = "__init__"
    def_code += (func_name + "(")
    if "argument" in keys:
        while len(args)>1:
            def_code += (args.pop(0) + ",")
        try:
            def_code += args.pop(0) + "):"
        except IndexError:
            def_code += "):"
    
    if not ("argument" in namelist):
        def_code += "):"
    
    return def_code

def getClass(lst):
    global N_indent
    args = []
    keys = []
    cls_code = ""
    for i in range(len(lst)):
        word = lst[i]
        if word.type == "KEY":
            if word.name == "for":
                word = KeyWord("four","NUM")
            elif word.name=="to":
                word = KeyWord("two","NUM")
            else:
                keys.append(word.name)
        if word.type == "ARG":
            args.append(word.name)
        if word.type == "NUM":
            if lst[i-1].type == "ARG" :
                args[len(args)-1] += str(WordToNumber[word.name])
    if not args:
        print("\nMissing class name.\nPlease add: ")
        AudioRecord("getclassname.pcm",4)
        cls_name = AipRecognize("getclassname.pcm")[0]
    else:
        if len(args)>1:
            print("\nMore than 1 class name detected.\nPlease redo: ")
            AudioRecord("getclassname.pcm",4)
            cls_name = AipRecognize("getclassname.pcm")[0]
        else:
            cls_name = args[0]
    
    cls_code += ("class "+cls_name+"():")
    return cls_code

def getExpress(lst,islogic=False):
    express = ""
    index = False
    left_bracket = True
    for i in range(len(lst)):
        word = lst[i]
        if word.type == "ARG":
            if word.name=="a":
                continue
            if word.name == "south":
                word.name = "self"
            if word.name=="egg" or word.name=="eggs" or word.name=="acts" or word.name=="ask": 
                word.name = "x"
            if word.name=="why":
                word.name = "y"
            if word.name=="tribute" or word.name=="attributes":
                word = KeyWord("attribute","OPR")
            if word.type=="ARG":
                express += word.name
            if index:
                express += "]"
            index = False
            
        if word.type == "OPR":
                
            if word.name == "is":
                if islogic:
                    express += "=="
                else:
                    express += "="
            elif word.name == "index":
                express += "["
                index = True
            elif word.name == "bracket":
                left_bracket = not left_bracket
                if left_bracket:
                    express += "("
                else:
                    express += ")"
            else:
                express += OpDict[word.name]
            continue
        if word.type == "NUM":
            express += str(WordToNumber[word.name])
            if index:
                express += "]"
                index = False
        
        if word.type == "KEY":
            if word.name == "for":
                express += "4"
            if word.name=="to":
                express += "2"
    return express

def getLogic(lst):
    condition = ""
    head = lst[0]
    if head.name=="if":
        condition += "if "
        lst.pop(0)
    elif head.name =="else":
        if lst[1].name=="if":
            condition += "elif "
            lst = lst[2:]
        else:
            return "else: "
        
    return getExpress(lst,islogic=True)
    
        
        
            
    




















