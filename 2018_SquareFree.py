# =====================
# PROGRAM : Square Free
# =====================

# Input :
n = int(input())


def fib(term):
    '''find n th fib num'''
    if term in [1,2]:
        return 1
    else:
        return fib(term-1) + fib(term-2)


def isPrime(num):
    '''check num is prime'''
    if num in [0, 1]:
        return False
    else:
        for div in range(2, int(num**0.5) + 1):
            if num%div==0:
                return False
        return True

def isSqrFree(num):
    '''check num is square free'''
    for div in range(1, int(num**0.5) + 1):
        if num%(div**2)==0 and isPrime(div**0.5):
            print(div)
            return False
    else:
        return True
            

nFib = fib(n)
if isSqrFree(nFib):
    print('YES')
else:
    print('NO')

