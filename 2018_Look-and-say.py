# ======================
# PROGRAM : Look-and-say
# ======================

# ---------
# Method 01
# ---------
from itertools import groupby

def nextTermGen(term):
    """Generate the next term"""
    strTerm = str(term)
    gen = ''
    for a,b in groupby(strTerm):
        tempList = list(b)
        gen += str(len(tempList)) + tempList[0]
    return int(gen)


def nTermGen(start):
    """Generate the n th term"""
    temp = start
    for _ in range(n-1):
        temp = nextTermGen(temp)
    nTerm = temp
    return nTerm

# Inputs:
m = int(input())
n = int(input())
##
##nTerm = nTermGen(m)
##
### Output:  
##print(nTerm)

# -------------------------------
# Method 02 (for 'nextTermGen()')
# -------------------------------

##term = 11222
##
##def nextTermGen(term):
##    tempStr = str(term)
##    point = 0
##    temp = 0
##    crntCount = 0
##    out = ''
##
##    while point<len(tempStr):
##        if tempStr[point]!=tempStr[temp]:
##            out += f'{crntCount}{tempStr[temp]}'
##            crntCount = 0   
##            temp = point
##        crntCount += 1
##        point += 1
##    
##    out += f'{crntCount}{tempStr[temp]}' # to add last items to result
##    return out