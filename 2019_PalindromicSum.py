# ===================================================
# PROGRAM : Palindromic Squars and Palindromic Primes
# ===================================================

# check 'n' is Palindromic
def isPal(n):
    return str(n)==str(n)[::-1]

# check 'n' is Square
def isSqr(n):
    return n**0.5==int(n**0.5)

# check 'n' is Prime
def isPrime(n):
    if n in [0,1]:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

a, b = map(int, input().strip().split()) # inputs
palSum = 0 # required sum

for x in range(a, b+1):
    if isPal(x) and (isSqr(x) or isPrime(x)):
        palSum += x

print(palSum) # output
