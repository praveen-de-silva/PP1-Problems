# ==========================
# PROGRAM : Find n th Number
# ==========================

def nTerm(term):
    '''recursive method to find n th term'''
    if term==0:
        return 0
    elif term==1:
        return 4
    else:
        return (3*(term+1)*(term+3)*nTerm(term-1) - 2*(term+2)*(term+3)*nTerm(term-2)) // ((term+1)*(term+2))

# --------------------------

while True:
    # Input :
    userInp = input().strip()

    if userInp=='-1': # terminating condition
        break
    else:
        try:            
            reqTerm = int(userInp)
            result = nTerm(reqTerm)
        except:
            print('Invalid Input!')
        else:
            # Output :
            print(result)
