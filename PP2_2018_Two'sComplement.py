def toBin(num):
    '''convert num to binary'''
    quo = num
    bin_rev = ''
    
    while True:
        if quo==0: # terminates when quotiant = 0
            break

        bin_rev += str(quo%2)
        quo //= 2
    return bin_rev[::-1].rjust(8, '0') # return 8 bit binary representation 

def invert(num_str):
    '''inverting the given binary format'''
    new_num_str = ''
    
    for char in num_str:
        if char=='0':
            new_num_str += '1'
        else:
            new_num_str += '0'
    return new_num_str

def addOne(bin_str):
    '''adding one to the given binary'''
    adding = 1
    result_rev = ''
    
    for i in range(7, 0, -1):
        temp_sum = int(bin_str[i]) + adding
        result_rev += str(temp_sum%2)
        adding = temp_sum//2

    result_rev += bin_str[0]
    return result_rev[::-1]

def twosComp(num):
    '''returns Two's Complement'''
    abs_num = abs(num)              # 1. get the absolute value of required number
    num_bin = toBin(abs_num)        # 2. converting it to the binary 
    num_bin2 = invert(num_bin)      # 3. inverting process
    num_two_comp = addOne(num_bin2) # 4. Two's Complement
    return num_two_comp
    

if __name__=='__main__':
    # Open files
    file_inp = open(input().strip(), 'r') # Input file
    file_out = open('Output.txt', 'w') # Output file

    # Output 
    file_int = int(file_inp.readline().strip()) # read data line-by-line
    result = twosComp(file_int) # Result
    print(result)
    file_out.write(result)

    # Close files
    file_inp.close()
    file_out.close()
