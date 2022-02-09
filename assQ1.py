# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def start(c):  
    if (c == 0):  
        dfa_state = 1
    elif (c == 1):  
        dfa_state = 0
    else:  
        dfa_state = -1
    return dfa_state 
 
def state1( c):

    if (c == 0):
        dfa_state = 2

    elif (c == 1):
        dfa_state = 0
    
    else:
        dfa_state = -1
    return dfa_state 

  
def state2(c):

    if (c == 1):
        dfa_state = 3
    
    elif (c == 0):
        dfa_state = 2
    
    else: 
        dfa_state = -1
    return dfa_state 
    
def state3(c):

     if (c == 0):
        dfa_state = 2
    
     elif (c == 1):
        dfa_state = 1
    
     else: 
        dfa_state = -1
     return dfa_state 
 
def DFA(str):
    dfa_state = 0
    for i in range(len(str)):
        if dfa_state == 0:
           dfa_state = start(str[i])
        elif dfa_state == 1:
           dfa_state = state1(str[i])
        elif dfa_state == 2:
           dfa_state = state2(str[i])
        elif dfa_state == 3:
           dfa_state = state3(str[i])
        else:
            return 0
  
       
    if dfa_state == 3:
        return 1
    else:
        return 0 
 

str = [ 1,0,0,1,0,1]
if DFA(str):
    print("Accepted")
else:
    print("Rejected")
   
            

                
        
             