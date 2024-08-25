# ===================
# PROGRAM : k-bonnaci
# ===================

# Inputs :
k = int(input())
n = int(input())

# ---------
# Method 01
# ---------

def nKFib(k, n):
    '''Find n th number of suquence'''
    terms = [] # to contain terms
    T = 1

    while True:
        if T==n:
            terms.append(sum(terms[T-1-k:])) # last term
            return terms[-1]
        elif T in range(1, k+1):
            terms.append(1) # first k terms
        else:
            terms.append(sum(terms[T-1-k:])) 
                
        T += 1
        
nTerm = nKFib(k, n)

# Output :
print(nTerm)



# ----------------------------
# Method 02 : Recursion Method
# ----------------------------

##def kFib(n):
##    if n in range(1, k+1):
##        return 1
##    else:
##        result = 0
##        for i in range(n-1,n-k-1, -1):
##            result += kFib(i)
##        return result
##
##print(kFib(n))