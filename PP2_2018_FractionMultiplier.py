def fracMul(num, frac):
    mul_val = num * frac

    if mul_val%1==0:
        return mul_val
    return False


def getResult(k, frac_arr):
    for _ in range(49):
        if k==1:
            break

        for frac in frac_arr:
            mul = fracMul(k, frac)
            if mul != False:
                k = int(mul)
                break
        else:
            break
    return k


if __name__=='__main__':
    file_inp = open(input().strip(), 'r')
    file_out = open('Output.txt', 'a')
    result = ''

    while True:
        inp_data = file_inp.readline().strip()

        if inp_data=='':
            break

        k_val, arr = map(eval, inp_data.strip().split('|'))
        result += f'{getResult(k_val, arr)}\n'

    file_out.write(result)
    print(result)

    file_inp.close()
    file_out.close()
