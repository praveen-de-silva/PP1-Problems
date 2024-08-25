# ========================
# PROGRAM : Obtuse Trangle
# ========================

from itertools import combinations as comb
from itertools import permutations as perm
import math


def decideLengths(tri):
    '''decides lengths for the input'''
    lengths = []
    twoPointsList = list(comb(tri,2))
    
    for twoPoints in twoPointsList:
        lengths.append(math.sqrt((twoPoints[1][0]-twoPoints[0][0])**2 + (twoPoints[1][1]-twoPoints[0][1])**2))

    lengths.sort()
##    print(lengths)
    return lengths


def isObtuse(tri):
    '''determine is obtuse'''
    lengths = decideLengths(tri) 
    a,b,c = lengths # get 3 sides of the triangle
    cosC = (a*a + b*b - c*c)/(2*a*b) # cosine of the obtuse angle

    if cosC<0:
        return True
    return False


# Input :
points = [[0,0], [0,1], [1,0], [-1,2], [3,4]]
##while True:
##    userInp = input().strip()
##    
##    if userInp=='-1':
##        break
##    
##    points.append(list(map(int, userInp.split())))
        
triPoints =  list(comb(points, 3))

obtuseCount = 0
for triangle in triPoints:
    if isObtuse(triangle):
        print(triangle)
        obtuseCount += 1

# Ouput :       
print(obtuseCount)
