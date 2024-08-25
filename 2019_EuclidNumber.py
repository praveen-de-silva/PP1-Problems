# =======================
# PROGRAM : Euclid Number
# =======================

# check 'n' is Prime
def isPrime(n):
    if n in [0,1]:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

n = int(input())

term = 0
i = 1
primeMul = 1 # initial multiplication

while True:
    if isPrime(i):
        primeMul *= i
        term += 1

    if term==n:
        break # terminat after n primes

    i += 1
    
euclidNum = primeMul + 1
print(euclidNum) # output
