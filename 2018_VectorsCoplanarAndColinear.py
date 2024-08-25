# =======================================
# PROGRAM : Vectors Coplanar and Colinear
# =======================================

class vector:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def mod(self):
        '''returns the modulus'''
        return (self.x**2 + self.y**2 + self.z**2)**0.5

def substract(vect1, vect2):
    '''substract 02 vectors'''
    resultVect = vector()
    resultVect.x = vect1.x-vect2.x
    resultVect.y = vect1.y-vect2.y
    resultVect.z = vect1.z-vect2.z 
    return resultVect

def crossProd(vect1, vect2):
    '''Cross Product of 02 vectors'''
    resultVect = vector()
    resultVect.x = vect1.y*vect2.z - vect1.z*vect2.y
    resultVect.y = vect1.z*vect2.x - vect1.x*vect2.z
    resultVect.z = vect1.x*vect2.y - vect1.y*vect2.x
    return resultVect

def dotProd(vect1, vect2):
    '''Dot Product of 02 vectors'''
    resultVal = vect1.x*vect2.x + vect1.y*vect2.y + vect1.z*vect2.z
    return resultVal

def triplProd(vect1, vect2, vect3):
    '''Triple Product of 02 vectors'''
    resultVal = dotProd(vect1, crossProd(vect2, vect3))
    return resultVal

def isCoplanar(vect1, vect2, vect3):
    '''check on same plane'''
    if triplProd(vect1, vect2, vect3)==0: return True
    return False


if __name__=='__main__':
    vectO = vector()
    vectA = vector()
    vectB = vector()
    vectC = vector()
    
    try:
        vects = [vectO, vectA, vectB, vectC]
        for vect in vects:
            vect.x, vect.y, vect.z = list(map(int, input().strip().split()))
    except:
        print('Invalid Input!')
    else:
        vectOA = substract(vectA, vectO)
        vectOB = substract(vectB, vectO)
        vectOC = substract(vectC, vectO)

        vectAB = substract(vectB, vectA)
        vectBC = substract(vectC, vectB)

        if isCoplanar(vectOA, vectOB, vectOC):
            if crossProd(vectOA, vectAB).mod()==0 and crossProd(vectAB, vectBC).mod()==0:
                print('All the points are colinear')
            else:
                print('On the same plane')
        else:
            print('Not on the same plane')
