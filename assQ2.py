# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:54:19 2021

@author: User
"""

def stateA(c):  
    if (c == "a"):  
        dfa_state = "c"
    elif (c == "b"):  
        dfa_state = "a"
    elif (c == "c"):  
        dfa_state = "b"
        
    else:  
        dfa_state = -1
    return dfa_state 
 
def stateB(c):

    if (c == "a"):
        dfa_state = "b"
    elif (c == "b"):
        dfa_state = "c"
    elif (c == "c"):
        dfa_state = "a"
    else:
        dfa_state = -1
    return dfa_state 

  
def stateC(c):

    if (c == "a"):
        dfa_state = "c"
    elif (c == "b"):
        dfa_state = "b"
    elif (c == "c"):
        dfa_state = "c"
    else: 
        dfa_state = -1
    return dfa_state 
    

 
def NFA(str):
    dfa_state = str[0]
    for i in range(len(str)-1):
            if dfa_state == "a":
                dfa_state = stateA(str[i+1])
            elif dfa_state == "b":
                dfa_state = stateB(str[i+1])
            elif dfa_state == "c":
                dfa_state = stateC(str[i+1])
            else:
                return 0
        
            
       
    if dfa_state == "a" or dfa_state == "b" or dfa_state == "c":
       return dfa_state
       
    else:
        return 0
    
 

str = [ "a" , "c" ]

if NFA(str) == NFA(str [::-1]):
    print("Accepted")
    
else:
    print("Rejected")
  
   
            

                
        
             
    