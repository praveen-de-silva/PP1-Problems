def isPrime(num):
    if num in [0,1]:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num%i==0:
            return False
    return True

def isPrimeFact(dev, num):
    if num%dev==0 and isPrime(dev):
        return True
    return False


if __name__ == '__main__':
    file_inp = open(input().strip(), 'r')
    file_out = open('Output.txt', 'w')

    file_data = file_inp.readline().strip()
    ints = list(map(int, file_data.split())) 
    out = ''

    for num in ints:
        temp_num = num
        prime_factors = []


        while True:
            for div in range(2, temp_num+1):
                if isPrimeFact(div, temp_num):
                    prime_factors.append(div)
                    temp_num = temp_num//div
                    break
            if temp_num==1:
                break

        out += '[' + ','.join([str(x) for x in prime_factors]) + ']\n'

    file_out.write(out)
    print(out)

    file_inp.close()
    file_out.close()
     
    
        
