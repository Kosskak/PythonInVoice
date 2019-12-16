# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:55:52 2019

@author: zyb32
"""
from tkinter import *
import threading
from dictate import Dictate
   
    
def StartDictation(time):
    global text,thread
    thl = threading.Lock()
    thread = Dictate(thl,text,time)
    thread.start()


def Copy(event=None):
    global text
    text.tag_add(SEL,"1.0",END)
    text.event_generate("<<Copy>>")

def Quit():
    global root,thread
    thread.stop()
    root.destroy()
    
    
def piv(time=3.8):
    global text,root
    root=Tk()                                                           
    root.title("TEST")
    m = Menu(root)
    root.config(menu=m)
    S_menu = Menu(m)
    text=Text(root)        
    text.pack()
    m.add_cascade(label="PIV",menu=S_menu)
    S_menu.add_command(label="Start Dictation",command=lambda:StartDictation(time))             
    S_menu.add_command(label="Copy Code",command=Copy) 
    S_menu.add_command(label="Quit",command=Quit)            
    root.mainloop()









