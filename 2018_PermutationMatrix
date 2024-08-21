# ============================
# PROGRAM : Permutation Matrix
# ============================

def matMaker(elements, n):
    '''make the matrix'''
    newMat = []
    for i in range(n):
        newMat.append(matElmnts[i*n : (i+1)*n])
    return newMat

def isPermMat(matrix):
    '''check whether is Permutation Matrix'''
    colIndexes = []

    for row in matrix:
        crntColInd = row.index(1)
        if row.count(1)==1 and crntColInd not in colIndexes:
            colIndexes.append(crntColInd)
        else:
            return 'NO'
    else:
        return 'YES'


# Inputs :
n = int(input())   
matElmnts = list(map(int, input().strip().split(',')))


mat = matMaker(matElmnts, n) # make the inputs to matrix


# Output :
print(isPermMat(mat))