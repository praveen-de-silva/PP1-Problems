def gen(arr):
    '''generate all the boolean posibilities'''
    if arr==[]:
        arr.extend([0,1])
        return arr
    
    else:
        originalArr = arr[:]
        arr.clear()

        for val in originalArr:
            for i in range(2):
                if type(val)==int:
                    tempVal = [val]
                else:
                    tempVal = val[:]
                tempVal.append(i)
                arr.append(tempVal)
                
        return arr

def solve(arr):
    '''get the result in each case'''
    res = []
    for items in arr:
        tempResult = items[0]
        for i in range(1, len(items)):
            tempResult ^= items[i] # find the 'XOR' value as the result
        res.append(tempResult)

    return res 
        
def findVarSize(data):
    '''find all the variable sizes'''
    sizes = []
    for x in data:
        sizes.append(len(x))

    return sizes

def setOutput():
    '''make the string of the Truth Table'''
    # line
    line = '+'
    for x in varSizes:
        line += '-'*x + '+'

    # topics
    topics = '|'
    for x in varNames:
        topics += x + '|'

    # body
    body = ''
    for i in range(len(boolVals)):
        body += '|'
        for j in range(len(boolVals[i])):
            body += str(boolVals[i][j]).ljust(varSizes[j], ' ') + '|'
        body += str(results[i]) + '|\n'

    outputStr = line + '\n' + topics + '\n' + line + '\n' + body + line
    return outputStr


try:
    # open files
    fileR = open(input().strip(), 'r')
    fileW = open('Output,txt', 'w')

    try:
        # Varables :               
        countVars = int(fileR.readline().strip())
        varNames = fileR.readline().strip().split() + ['Y']
        varSizes = findVarSize(varNames)


        # make the Truth Table
        boolVals = []
        for _ in range(countVars):
            gen(boolVals)

        results = solve(boolVals)
        outputStr = setOutput()

    except Exception:
        print('Data error!')

    else:
        print(outputStr)
        # add data to files
        fileW.write(outputStr)
        
    finally:
        # close the files
        fileR.close()
        fileW.close()

    
except FileNotFoundError:
    print('File does not exist!')
    
