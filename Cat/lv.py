#adapted from https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/

import numpy as np

ts = 1
tv = 3
g  = 5

u = ['A','G']
y = ['T','C']

def twod(s1,s2):
    
    dt = np.zeros((len(s1) + 1, len(s2) + 1))
    
    for i in range(len(s1) + 1):
        dt[i] = i*g
        
    for i in range(len(s2) + 1):
        dt[0][i] = i*g
        
    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):    
            
            if (s1[i1-1] == s2[i2-1]):
                dt[i1][i2] = dt[i1 - 1][i2 - 1]
            
            elif (s1[i1-1] in u) ^ (s2[i2-1] in u):
                dt[i1][i2] = min(dt[i1][i2-1], dt[i1-1][i2], dt[i1-1][i2-1]) + ts
            else:
                dt[i1][i2] = min(dt[i1][i2-1], dt[i1-1][i2], dt[i1-1][i2-1]) + tv
                
                
        
    printDistances(dt, len(s1), len(s2))
    return dt[len(s1)][len(s2)]
        
        
def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()