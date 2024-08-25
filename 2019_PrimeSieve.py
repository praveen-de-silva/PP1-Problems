# =====================
# PROGRAM : Prime Sieve
# =====================

# Input :
upLim = int(input())


def genPrimes(upLimit):
    '''generate primes by Prime Sieve method'''
    grid = list(range(1, upLimit + 1))
    primes = grid[:] # get a copy of grid

    primes.remove(1) # Step 01 : remove '1'

    i = 0
    while True:
        if i==len(primes):
            break
        
        key = primes[i]

        for x in primes[i:]:
            if x%key==0 and x!=key:
                primes.remove(x) # Steps 02 to 06 : leave the num and remove it's multiples        
        i+=1
        
    return primes


if __name__=='__main__':
    try:
        primes = genPrimes(upLim)
        primesStr = [str(x) for x in primes]
    except:
        print('Error!')
    else:
        # Output :
        print(' '.join(primesStr))
