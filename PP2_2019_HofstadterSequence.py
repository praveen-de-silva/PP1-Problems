def F(n):
    if n==0:
        return 1
    return n - M(F(n-1))

def M(n):
    if n==0:
        return 0
    return n - F(M(n-1))


if __name__=='__main__':
    # == Open Files ==
    file_inp = open(input().strip(), 'r')
    file_out = open('Output.txt', 'w')
    res = '' # string to contain the result

    while True:
        file_data = file_inp.readline().strip()

        if file_data == '':
            break

        crnt_int = int(file_data)
        crnt_out = f'{crnt_int}: F={F(crnt_int)} M={M(crnt_int)}' + '\n' # get the resultant srtatement for each integer
        res += crnt_out

    # == Output ==
    file_out.write(res)
    print(res)

    # == Close Files ==
    file_inp.close()
    file_out.close()
