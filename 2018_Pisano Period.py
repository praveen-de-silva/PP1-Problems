# =======================
# PROGRAM : Pisano Period
# =======================

fibSeq = [0, 1] # fib list

def fibSeqGen(m):
    '''Generate the Fibonacci Sequence'''
    global fibSeq # use global list
    termA = 0
    termB = 1
    
    for i in range(m-2):
        termNext = termA + termB 
        fibSeq += [termNext]

        termA = termB
        termB = termNext

def pisPeriod(n):
    '''Find n th Pisano Period'''
    moded = [x%n for x in fibSeq]
    i = 1 # initial period
    
    while 2*i<=52:
        if moded[:i] == moded[i:2*i]:
            return i
            break
        i += 1
    return None
     
fibSeqGen(50) # generate fib list upto 50 terms


# User Input:
n = int(input().strip()) 

# Output
print(pisPeriod(n))