# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:23:21 2019

@author: zyb32
"""
import threading
import ctypes
import inspect
from main import PIVmain
from tkinter import INSERT
from get_code import getCode

class Dictate(threading.Thread):
    
    def __init__(self,lock,text,time):
        threading.Thread.__init__(self)
        self.threadLock = lock
        self.text = text
        self.time = time
    def run(self):
        self.threadLock.acquire()
        generator = PIVmain(self.time)
        for code_list in generator:
            self.text.delete('1.0','end')
            code = getCode(code_list)
            self.text.insert(INSERT,code)
        self.threadLock.release()

    def stop(self,exctype=SystemExit):
        tid = ctypes.c_long(self.ident)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed") 
            
            
            
            
            
            
            
            
            
            
            
            