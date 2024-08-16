# =================================
# PROGRAM : Sum of Bouncing Numbers
# =================================

# check 'n' is Increasing
def isInc(n):
    num = str(n) # create a string to iterate and analyze

    tempMax = num[0]

    for point in num:
        if int(point)>=int(tempMax):
            tempMax=point
        else:
            return False
    return True

# check 'n' is Decreasing
def isDec(n):
    num = str(n) # create a string to iterate and analyze

    tempMin = num[0]

    for point in num:
        if int(point)<=int(tempMin):
            tempMin=point
        else:
            return False
    return True

# check 'n' is Bouncing
def isBnc(n):
    if n in range(100):
        return False
    return not(isInc(n) or isDec(n))

p, q = map(int, input().strip().split()) # Inputs
bncSum = 0 

# calculating the sum
for x in range(p, q+1):
    if isBnc(x):
        bncSum += x 

print(bncSum) # Output