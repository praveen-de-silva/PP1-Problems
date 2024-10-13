def searchX(arr, X_val):
    X_index = []
    i = 0
    while i<len(arr):
        if arr[i]==X_val:
            X_index.append(i)
        i += 1
    return X_index

def searchY(arr, Y_val):
    Y_index = []
    j = 0
    while j<len(arr):
        if arr[j]==Y_val:
            Y_index.append(j)
        j += 1
    return Y_index

def rearrange(arr_A, X, Y):
    X_indexes = searchX(arr_A, X)
    Y_indexes = searchY(arr_A, Y)
    arr_B = arr_A.copy()

    for k in range(len(X_indexes)):
        if X_indexes[k] < len(arr_B)-1:
            arr_B[X_indexes[k] + 1], arr_B[Y_indexes[k]] = arr_B[Y_indexes[k]], arr_B[X_indexes[k] + 1]
        else:
            arr_B[X_indexes[k]], arr_B[Y_indexes[k]] = arr_B[Y_indexes[k]], arr_B[X_indexes[k]]
    return arr_B


if __name__=='__main__':
    file_inp = open(input(), 'r')
    file_out = open('Output.txt', 'a')
    res = ''

    while True:
        data = file_inp.readline()

        if data=='':
            break

        arr, X, Y = map(eval, data.strip().split())
        res += str(rearrange(arr, X, Y)) + '\n'

    file_out.write(res)
    print(res)


    file_inp.close()
    file_out.close()
